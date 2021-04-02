import pandas as pd
import re
import string
import unicodedata
import nltk
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary
from nltk.tokenize import word_tokenize

def clean_text(kata):
    #lowercase
    kata = kata.lower()
    #remove number
    kata = re.sub(r"\d+", "", kata)
    # remove punctuation
    kata = kata.translate(str.maketrans("","",string.punctuation))
    #remove spaces
    kata = kata.strip()
    # remove link
    kata = re.sub(r"http\S+", "", kata)
    # remove hashtag
    kata = kata.replace('#', '')
    # remove @
    kata = kata.replace('@', '')
    # remove non ascii chars
    new_words = []
    for word in kata:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    kata = "".join(new_words)
    return kata

#replace string
def find_replace(kata, kalimat):
    list_to_replace = kalimat.split()
    for i,word in enumerate(list_to_replace):
        if kata in word:
            list_to_replace[i] = kata
    return " ".join(list_to_replace)

def remove_stopwords_id(kalimat):    
    # ambil stopword bawaan
    stop_factory = StopWordRemoverFactory().get_stop_words()
    more_stopword = ['daring', 'online', 'nih']

    # menggabungkan stopword
    data = stop_factory + more_stopword

    dictionary = ArrayDictionary(data)
    string = StopWordRemover(dictionary)
    tokens = nltk.tokenize.word_tokenize(string.remove(kalimat))
    return(" ".join(tokens))
