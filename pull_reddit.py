import requests


class PullReddit:
  def __init__(self, subreddit):
    self.subreddit = subreddit

  def get_top_titles(self):
    posts = self.__get_top_posts_data()
    titles = []
    for post in posts:
      titles.append(post['data']['title'])
    return titles

  def __get_top_posts_data(self):
    url = "https://api.reddit.com/r/" + self.subreddit + "/top?t=100&limit=100"
    response = requests.get(url, headers={'Content-Type': 'application/json', 'User-agent': 'nishant-mac'})
    posts = response.json()['data']['children']
    return posts 
