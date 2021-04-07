from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from pre_process import *
from calculate_sentiment import sentimentTextBlob
from vect_tfidf import vectorize
from log_reg_sentiment import predict

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        "text": "mantap! siap digeber"
        }
    return jsonify(data), 200  

@app.route('/process', methods = ['POST'])
def process():
    tweet = request.json['tweet']
    # kata = clean_text(tweet)
    # kata = find_replace('indihome', kata)
    # kata = remove_stopwords_id(kata)
    vectorized_text_df = vectorize(tweet)
    # sentiment = sentimentTextBlob(vectorized_text_df)
    sentiment = predict(vectorized_text_df)
    data = {
        "tweet": tweet,
        "sentiment": str(sentiment),
        }
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0')
