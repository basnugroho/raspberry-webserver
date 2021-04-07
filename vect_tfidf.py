from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pickle
from pre_process import *

# load the model from disk
#Load tfidf
transformer = TfidfTransformer()
loaded_vec = CountVectorizer(decode_error="replace",vocabulary=pickle.load(open("feature.pkl", "rb")))

def vectorize(text):
    cleaned_text = remove_stopwords_id(clean_text(text))
    cleaned_text_ls = pd.Series([cleaned_text])
    tfidf = transformer.fit_transform(loaded_vec.fit_transform(cleaned_text_ls))
    # transform to an array
    cleaned_text_array = tfidf.toarray()
    #transofrm back to a dataframe, assign column values
    cleaned_text_num_df = pd.DataFrame(cleaned_text_array, columns=loaded_vec.get_feature_names())
    return cleaned_text_num_df
