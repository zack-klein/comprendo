from compo import explore_topic


def _make_response(code, msg=None, result=None):
    return code, {
        "error": code > 299,
        "msg": msg,
        "result": result or {},
    }


def handler(event, context):
    topic = event.get("topic")
    num_tweets = event.get("num_tweets", 500)
    max_results_per_item = event.get("max_results_per_item")

    if not all([topic, num_tweets]):
        code, response = _make_response(
            400, msg="Bad request! Must have at least topic, num_tweets."
        )
    else:
        status_code, body = explore_topic(
            topic,
            num_tweets=num_tweets,
            max_results_per_item=max_results_per_item,
        )
        code, response = _make_response(
            status_code,
            msg="Successfully fetched!" if status_code == 200 else "Error!",
            result=body,
        )

    return {
        "statusCode": code,
        "body": response,
    }
