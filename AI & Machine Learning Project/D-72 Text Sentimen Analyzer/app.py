from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    if blob.sentiment.polarity > 0:
        return "Positif"
    elif blob.sentiment.polarity < 0:
        return "Negatif"
    else:
        return "Netral"

# Example 
text = "I love this product!"
sentimen = analyze_sentiment(text)
print(f"Teks: {text}")
print(f"Sentimen: {sentimen}")