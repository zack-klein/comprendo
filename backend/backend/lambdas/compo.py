import logging
import os
import boto3
import statistics

import tweepy


def get_entities(texts, language, max_results_per_item=None):
    client = boto3.client("comprehend")
    results = []
    batch = []
    counter = 0

    while texts:
        if counter == 25:
            response = client.batch_detect_entities(
                TextList=batch, LanguageCode=language
            )
            results.append(response)
            batch = []
            counter = 0

        batch.append(texts.pop())
        counter += 1

    # We may have leftovers in the last batch
    if batch:
        response = client.batch_detect_entities(
            TextList=batch, LanguageCode=language
        )
        results.append(response)

    # Clean up the results
    clean_entities = clean_up_results(
        results, max_results=max_results_per_item
    )

    return clean_entities


def clean_up_results(results, max_results=None):
    entities = {}

    # First, we need to combine the results
    for result in results:
        result_list = result.get("ResultList")
        for doc in result_list:
            all_entities = doc.get("Entities")
            for entity in all_entities:
                entity_type = entity.get("Type")
                entity_text = entity.get("Text")
                entity_score = entity.get("Score")
                entity_d = {
                    "text": entity_text,
                    "score": round(entity_score * 100, 2),
                }
                existing = entities.get(entity_type, [])
                existing.append(entity_d)
                entities[entity_type] = existing

    # Next we want to consolidate each item
    consolidated_entites = {}
    for ent_type, ents in entities.items():
        seen = {}
        for ent in ents:
            cleaned_entity_name = (
                ent["text"].lower().replace(".", "").title()
            )
            existing_entity = seen.get(cleaned_entity_name)

            if existing_entity:
                # Bump occurrences, and recalculate the average score
                # Occurrences
                this_ent = existing_entity
                occurrences = this_ent["occurrences"] + 1
                this_ent["occurrences"] = occurrences

                # Scores
                new_scores = this_ent["scores"]
                new_scores.append(ent["score"])
                new_avg = statistics.mean(new_scores)
                this_ent["scores"] = new_scores
                this_ent["avg_scores"] = new_avg
            else:
                this_ent = {
                    "occurrences": 1,
                    "avg_score": ent["score"],
                    "scores": [ent["score"]],
                    "type": ent_type,
                    "text": cleaned_entity_name,
                }
            seen[cleaned_entity_name] = this_ent

        if not max_results:
            max_results = len(seen.values())
        seen_ents = list(seen.values())[:max_results]
        consolidated_entites[ent_type] = seen_ents

    # Next we want to sort the results by occurrences, then score descending
    for ent_type, ents in consolidated_entites.items():
        sorted_ents = sorted(
            ents,
            key=lambda i: (i["occurrences"], i["avg_score"]),
            reverse=True,
        )
        consolidated_entites[ent_type] = sorted_ents

    # Reformat so the frontend will accept the results
    clean_entities = {}
    for ent_type, ents in consolidated_entites.items():
        this_ent_type = clean_entities.get(ent_type, {})

        for ent in ents:
            this_ent_type[ent["text"]] = ent

        clean_entities[ent_type] = this_ent_type
    return clean_entities


def get_tweets(topic, num=500):
    auth = tweepy.AppAuthHandler(
        os.getenv("TWITTER_API_KEY"),
        os.getenv("TWITTER_API_SECRET_KEY"),
    )
    api = tweepy.API(auth)
    tweets = []
    for tweet in tweepy.Cursor(api.search, q=topic).items(num):
        if tweet.lang == "en":
            tweets.append(tweet.text)

    return tweets


def explore_topic(topic, num_tweets=500, max_results_per_item=None):
    try:
        tweets = get_tweets(topic, num=num_tweets)
        result = get_entities(
            tweets, "en", max_results_per_item=max_results_per_item
        )
        status_code = 200
    except Exception as e:
        logging.exception(e)
        result = str(e)
        status_code = 500

    return status_code, result
