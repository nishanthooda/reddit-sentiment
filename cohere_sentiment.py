import cohere
from cohere.responses.classify import Example


class CohereSentiment:
  def __init__(self, api_key):
    self.co = cohere.Client(api_key)

  def analyze_sentiment(self, titles, sample_positive_titles, sample_negative_titles):
    return self.co.classify(
      inputs=titles[:96],
      examples=self.__training_examples(sample_positive_titles, sample_negative_titles)
    )

  def __training_examples(self, positive_titles, negative_titles):
    examples = []
    for pos_title in positive_titles:
      examples.append(Example(pos_title, "positive"))
    for neg_title in negative_titles:
      examples.append(Example(neg_title, "negative"))
    return examples
