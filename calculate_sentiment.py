from textblob import TextBlob

def sentimentTextBlob(kata):
    all_polarity = 0
    analysis = TextBlob(kata)
    an = analysis.translate(from_lang='id', to='en')
    sentiment = "netral"
    all_polarity += an.polarity
    if (all_polarity/100 > 0):
        sentiment = "positive"
    elif (all_polarity/100 == 0):
        sentiment = "netral"
    else:
        sentiment = "negative"
    data = {
        "subjectivity": an.sentiment.subjectivity,
        "polarity": an.sentiment.polarity,
        "sentiment": sentiment
    }
    return data
