from flask import Flask, render_template, request, jsonify
import os
from tweet_processing import *

app = Flask(__name__, static_url_path='/static')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')
FILES_STATIC = os.path.join(APP_STATIC, 'files')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['get'])
def search():
    query = request.args.get("q")
    if query is None:
        return render_template('search.html')
    else:
        tweets = search_tweets('tweets.json', query)
        return jsonify(tweets)

@app.route('/wordcloud/<type>')
def wordcloud(type):
    if type == "freq":
        return generate_wordcloud_by_freq('tweets.json')
        



@app.route('/register', methods=['post'])
def register():
    name = request.form.get("name")
    session = request.form.get("session")
    print(name, session)
    if not name or not session:
        return "Failure"
    return render_template('success.html')
