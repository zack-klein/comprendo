const axios = require("axios");

const url =
  "https://pt69k9t1a5.execute-api.us-east-1.amazonaws.com/prod/comprendo";

export const TopicService = {
  fetchTopic: async (topic) => {
    const response = await axios.post(url, {
      topic: topic,
      num_tweets: 500,
      max_results_per_item: 10,
    });
    return response;
  },
};
