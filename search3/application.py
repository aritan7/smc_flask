from flask import Flask, render_template, request
from tweet_processing import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    q = request.args.get('q')
    if not q:
        return render_template('failure.html', tweets='Please enter some keywords.')
    tweets = get_tweet_text_by_keyword('tweets.json', keyword=q)
    if len(tweets) == 0:
        return render_template('failure.html', tweets='None. Please try again.')

    return render_template('results.html', tweets=tweets)
