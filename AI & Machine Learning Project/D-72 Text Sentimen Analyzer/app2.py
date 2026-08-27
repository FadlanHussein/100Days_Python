from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentimen_vader(text):
    scores = analyzer.polarity_scores(text)
    if scores["compound"] >= 0.05:
        return "Positif"
    elif scores["compound"] <= -0.05:
        return "Negatif"
    else:
        return "Netral"

# Example
text = "I love this product!"
sentimen = analyze_sentimen_vader(text)
print(f"Teks: {text}")
print(f"Sentimen: {sentimen}")