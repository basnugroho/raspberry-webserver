import re
import unicodedata
import nltk
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.tokenize import word_tokenize

def clean_text(kata):    
    # remove full urls
    kata = re.sub("https*\S+", "<URL>", kata)
    
    #lowercase
    kata = kata.lower()
    
    # remove full hastag
    # kata = re.sub("#\S+", " ", kata)
    
    #remove number
    # kata = re.sub(r"\d+", "", kata)
    
    # remove link
    # kata = re.sub(r"http\S+", "", kata)
    
    # remove hashtag
    # kata = kata.replace('#', '')
    
    # remove space >, <
    kata = kata.replace('< ', '<')
    kata = kata.replace(' >', '>')
    
    # remove punctuation
    # kata = kata.translate(str.maketrans("","",string.punctuation))
    
    #remove extra spaces
    kata = kata.strip()
    
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
    more_stopword = more_stopword = ['nih', 'sih', 'kok', 'hi', 'yah',
                'mohon', 'nya', 'yg', 'hai', 'wkwk', 'wkwkwk', 'wkwkwkwk']

    # menggabungkan stopword
    data = stop_factory + more_stopword

    dictionary = ArrayDictionary(data)
    string = StopWordRemover(dictionary)
    tokens = nltk.tokenize.word_tokenize(string.remove(kalimat))
    return(" ".join(tokens))

def stem_sastrawi(kalimat):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    return stemmer.stem(kalimat)

def replace_product(kata):
    kata = kata.lower()
    # from mention
    kata = re.sub("@biznet*\S+", "<PRODUCT_NAME>", kata)
    kata = re.sub("@indihome*\S+", "<PRODUCT_NAME>", kata)
    kata = re.sub("@di_cbn*\S+", "<PRODUCT_NAME>", kata)
    # from word
    kata = re.sub("indi*\S+", "<PRODUCT_NAME>", kata)
    kata = re.sub("indeh*\S+", "<PRODUCT_NAME>", kata)
    kata = re.sub("indieho*\S+", "<PRODUCT_NAME>", kata)
    return kata
    
def replace_provider(kata):
    kata = kata.lower()
    # from mention
    kata = re.sub("@telkom*\S+", "<PROVIDER_NAME>", kata)
    # from word
    kata = re.sub("indi*\S+", "<PROVIDER_NAME>", kata)
    kata = re.sub("telkomsel*\S+", "<PROVIDER_NAME>", kata)
    return kata

def replace_mention(kata):
    # remove full mentions
    kata = re.sub("@\S+", "<USER_MENTION>", kata)
    kata = kata.lower()
    return kata

def remove_bracket(kata):
    kata = re.sub("@\S+", "<USER_MENTION>", kata)