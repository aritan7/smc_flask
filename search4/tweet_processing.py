import os, json


def read_json_from_file(fname):
    # input fname as argument, return list of json documents
    with open(fname, 'r') as f:
        list_of_json = json.loads(f.read())
    return list_of_json


def get_tweet_text(fname):
    # input fname as argument, return a list of tweet-text,

    list_of_json = read_json_from_file(fname)
    list_of_tweets = []
    for json_doc in list_of_json:
        list_of_tweets.append(json_doc['text'])

    return list_of_tweets


def get_tweet_text_by_keyword(fname, keyword):
    # function to return list of tweet-text only if keyword is present

    list_of_tweets = get_tweet_text(fname)
    filtered_tweets = []
    for tweet in list_of_tweets:
        if keyword.lower() in tweet.lower():
            filtered_tweets.append(tweet)
    return filtered_tweets




### Sanity check ###
# print(read_json_from_file('tweets.json')[:5])
# print(get_tweet_text('tweets.json'))
# print(get_tweet_text_by_keyword('tweets.json', keyword='video'))