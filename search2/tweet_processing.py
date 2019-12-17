import os, json
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from wordcloud import WordCloud

STOPWORDS = set(stopwords.words('english'))

def read_json_from_file(fname):
    # input fname as argument, return dict
    with open(fname, 'r') as f:
        doc = json.loads(f.read())
    return doc

def get_tweets_only(fname):
    # input fname as argument, return list of tweets

    tweet_docs = read_json_from_file(fname)

    tweet_tokenizer = TweetTokenizer()
    tweet_tokens = [tweet_tokenizer.tokenize(doc['text']) for doc in tweet_docs]
    list_of_tweets = [' '.join(tweets) for tweets in tweet_tokens]
    return list_of_tweets

def search_tweets(fname, keyword):
    # function to return list of tweets if keyword is found 
    
    list_of_tweets = get_tweets_only(fname)
    return [tweet for tweet in list_of_tweets if keyword.lower() in tweet.lower()]

 

