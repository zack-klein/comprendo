from compo import explore_topic

from dotenv import load_dotenv

load_dotenv()

print(explore_topic("cancun", num_tweets=15, max_results_per_item=2))
