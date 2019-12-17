from flask import Flask, render_template, request
from tweet_processing import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    q = request.args.get('q')
    if not q:
        return render_template('failure.html', tweets="failure")
    tweets = search_tweets('tweets.json', keyword=q)
    return render_template('results.html', tweets=tweets)
