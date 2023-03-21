# Reddit-Sentiment

This python script tells you how positive the sentiment of the reddit homepage is so you know what you are in for. It leverages Cohere's classify library and uses the top 100 posts from the _/r/mademesmile_ and _/r/politics_ subreddits as postive and negative sentiment training data respectively.  

## How to use
1. clone repo locally
2. add an `.env` var file to your local repository that has your [cohere API key](https://docs.cohere.ai/reference/key) defined under the `COHERE_API_KEY` variable
3. run `python3 main.py`
