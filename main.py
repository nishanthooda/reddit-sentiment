import os

from dotenv import load_dotenv

from cohere_sentiment import CohereSentiment
from pull_reddit import PullReddit

load_dotenv()

positive_titles = PullReddit("mademesmile").get_top_titles()
negative_titles = PullReddit("politics").get_top_titles()
titles = PullReddit("all").get_top_titles()

co = CohereSentiment(os.environ.get('COHERE_API_KEY'))
sentiment_classifications = co.analyze_sentiment(titles, positive_titles, negative_titles)
total_pos = 0
total_neg = 0
for sentiment in sentiment_classifications:
  if sentiment.prediction == "positive":
    total_pos+=1
  elif sentiment.prediction == "negative":
    total_neg+=1

pos_percentage = total_pos/(total_pos+total_neg) * 100
print(f"The reddit homepage is {round(pos_percentage, 2)}% positive today!")
