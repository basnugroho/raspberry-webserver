from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from pre_process import *
from calculate_sentiment import sentimentTextBlob
from vect_tfidf import vectorize
from log_reg_sentiment import predict
from log_reg_kategori_ggn import predict_ggn
from flask_cors import CORS
# netezza
import nzpy

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    data = {
        "text": "mantap! siap digeber"
        }
    return jsonify(data), 200  

@app.route('/v1/sentiment/process', methods = ['POST'])
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

@app.route('/v1/netezza/telkomshare5', methods = ['POST'])
def telkomshare5():
    conn = nzpy.connect(user="USER_TR5_ROC", password="TR5_ROC#8635", host='10.62.187.9', port=5480, database="TELKOMSHARE5", securityLevel=1,logLevel=0)
    print(str(request.json['query']))
    query = str(request.json['query'])
    with conn.cursor() as cursor:
        try:
            cursor.execute(query)
            print(f"query for {0} succeed".format("telkomshare5"))
            results = cursor.fetchall()
            print(results)
            response = jsonify(results)
            return response
        except Exception as e:
            print(str(e))

@app.route('/v1/netezza/payments', methods = ['POST'])
def payments():
    conn = nzpy.connect(user="usr_tr5", password="newtelkom2018", host='10.62.187.9', port=5480, database="TELKOMPROD", securityLevel=1,logLevel=0)
    print(str(request.json['query']))
    query = str(request.json['query'])
    with conn.cursor() as cursor:
        try:
            cursor.execute(query)
            print(f"query for {0} succeed".format("TELKOMPROD"))
            results = cursor.fetchall()
            print(results)
            response = jsonify(results)
            return response
        except Exception as e:
            print(str(e))

@app.route('/v1/netezza/telkomparam', methods = ['POST'])
def telkomparam():
    conn = nzpy.connect(user="USER_TR5_ROC", password="TR5_ROC#8635",host='10.62.187.9', port=5480, database="TELKOMPARAM", securityLevel=1,logLevel=0)
    print(str(request.json['query']))
    query = str(request.json['query'])
    with conn.cursor() as cursor:
        try:
            cursor.execute(query)
            print(f"query for {0} succeed".format("telkomparam"))
            results = cursor.fetchall()
            print(results)
            response = jsonify(results)
            return response
        except Exception as e:
            print(str(e))
    conn.close()
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')
