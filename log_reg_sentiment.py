from sklearn.linear_model import LogisticRegression
import pickle

def predict(vectorized_text_df, model):
    # load the model from disk
    loaded_model = pickle.load(open(model, 'rb'))
    sentiment = loaded_model.predict(vectorized_text_df[:])
    return sentiment[0]