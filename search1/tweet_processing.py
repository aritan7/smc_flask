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

    #### Your Code here ####

    ######################

    return list_of_tweets

def search_tweets(fname, keyword):
    # function to return list of tweets if keyword is found 

    #### Your Code here ####

    ######################

    return list_of_tweets


 

