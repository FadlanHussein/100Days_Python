from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER Analyzer
analyzer = SentimentIntensityAnalyzer()

# Function using TextBlob
def analyze_sentiment_textblob(text):
    sentiment = TextBlob(text).sentiment.polarity

    if sentiment > 0:
        return "Positif"
    elif sentiment < 0:
        return "Negatif"
    else:
        return "Netral"

# Function using VADER
def analyze_sentiment_vader(text):
    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        return "Positif"
    elif compound <= -0.05:
        return "Negatif"
    else:
        return "Netral"

# Main Function
def analyze_user_input():
    while True:
        text = input("Enter a sentence for sentiment analysis (or type 'exit' to quit): ")

        if text.lower() == "exit":
            print("Exiting Sentiment Analyzer.")
            break

        print(f"TextBlob Sentiment: {analyze_sentiment_textblob(text)}")
        print(f"VADER Sentiment: {analyze_sentiment_vader(text)}")

# Run Application
if __name__ == "__main__":
    analyze_user_input()