import os, json
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from wordcloud import WordCloud



APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')
FILES_STATIC = os.path.join(APP_STATIC, 'files')

STOPWORDS = set(stopwords.words('english'))

def read_json_from_file(fname):
    with open(os.path.join(FILES_STATIC, fname), 'r') as f:
        doc = json.loads(f.read())
    return doc

def get_tweets_only(fname):
    tweet_docs = read_json_from_file(fname)

    tweet_tokenizer = TweetTokenizer()
    tweet_tokens = [tweet_tokenizer.tokenize(doc['text']) for doc in tweet_docs]
    list_of_tweets = [' '.join(tweets) for tweets in tweet_tokens]
    return list_of_tweets

def search_tweets(fname, keyword):
    list_of_tweets = get_tweets_only(fname)
    return [tweet for tweet in list_of_tweets if keyword.lower() in tweet.lower()]

 
def get_list_of_token(fname):
    list_of_tweets = get_tweets_only(fname)
    list_of_tokens = [word.lower() for tweet in list_of_tweets 
                                    for word in tweet.split(' ') 
                                    if word not in STOPWORDS and len(word) > 3 and not word.startswith('http')]
    return list_of_tokens

def generate_wordcloud_by_freq(fname):
    list_of_tweets = get_list_of_token(fname)
    wordcloud = WordCloud(stopwords=STOPWORDS, background_color='white', width=900, height=1000).generate(' '.join(list_of_tweets))
    save_fname = "wordcloud_freq.png"
    wordcloud.to_file(os.path.join(FILES_STATIC, save_fname))

    return save_fname


# TWEET_CONTENTS = read_json_from_file('tweets.json')
# print(search_tweets('tweets.json', "christmas"))
# print(generate_wordcloud_by_freq('tweets.json'))


