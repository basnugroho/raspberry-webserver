from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from pre_process import *
from calculate_sentiment import sentimentTextBlob
from vect_tfidf import vectorize
from log_reg_sentiment import predict
from log_reg_kategori_ggn import predict_ggn
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    data = {
        "text": "mantap! siap digeber"
        }
    return jsonify(data), 200  

@app.route('/process', methods = ['POST'])
def process():
    print(str(request.json['tweet']))
    tweet = str(request.json['tweet'])
    replaced_entitiy_text = remove_stopwords_id(replace_mention(replace_product(replace_provider(str(tweet)))))
    cleaned_text = clean_text(remove_stopwords_id(str(replaced_entitiy_text)))
    vectorized_text_df = vectorize(cleaned_text,'tfidf_model.pkl')
    # sentiment = sentimentTextBlob(vectorized_text_df)
    sentiment = predict(vectorized_text_df,'inet_model.sav')
    data = {}
    if sentiment < 0:
        kategori = predict_ggn(vectorized_text_df)
        data = {
            "tweet": tweet,
            "sentiment": str(sentiment),
            "kategori": str(kategori)
            }
        return jsonify(data), 200
    else:
        data = {
            "tweet": tweet,
            "sentiment": str(sentiment),
            }
        response = jsonify(data)
        print(response)
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
