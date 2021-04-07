from sklearn.linear_model import LogisticRegression
import pickle

# load the model from disk
loaded_model = pickle.load(open('leman_pos.sav', 'rb'))

def predict(vectorized_text_df):
    sentiment = loaded_model.predict(vectorized_text_df[:])
    return sentiment[0]