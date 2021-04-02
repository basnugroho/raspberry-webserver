from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from pre_process import *
from calculate_sentiment import sentimentTextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>yup! You are on the right page.</h1>'

@app.route('/process', methods = ['POST'])
def process():
    tweet = request.json['tweet']
    kata = clean_text(tweet)
    kata = find_replace('indihome', kata)
    kata = remove_stopwords_id(kata)
    sentiment = sentimentTextBlob(kata)
    data = {
        "tweet": tweet,
        "pre_process": kata,
        "sentiment": sentiment,
        }
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0')
