from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pickle
from pre_process import *
import pandas as pd

# load the model from disk
#Load tfidf
transformer = TfidfTransformer()

def vectorize(cleaned_text, vect_model):
    loaded_vec = CountVectorizer(decode_error="replace",vocabulary=pickle.load(open(vect_model, "rb")))
    cleaned_text_ls = pd.Series([cleaned_text])
    tfidf = transformer.fit_transform(loaded_vec.fit_transform(cleaned_text_ls))
    # transform to an array
    cleaned_text_array = tfidf.toarray()
    #transofrm back to a dataframe, assign column values
    cleaned_text_num_df = pd.DataFrame(cleaned_text_array, columns=loaded_vec.get_feature_names())
    return cleaned_text_num_df
