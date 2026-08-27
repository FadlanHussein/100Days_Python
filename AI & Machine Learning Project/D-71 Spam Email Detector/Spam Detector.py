import os
import pandas as pd 
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report


# Download Stopwords / Punkt
nltk.download("stopwords", quiet=True)
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))


# Load Dataset
file_path = os.path.join(os.path.dirname(__file__), "spam.csv")
df = pd.read_csv(file_path)[["label", "message"]]
df.columns = ["label", "text"]
df["label"] = df["label"].map({"spam": 1, "ham": 0})

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = word_tokenize(text)
    text = [stemmer.stem(word) for word in text if word not in stop_words]
    return " ".join(text)


# Apply the preprocess function
df["clean_text"] = df["text"].apply(preprocess_text)
print("=== Preprocessed Data ===")
print(df[["label", "clean_text"]].head())

# Feature Extraction with TF-IDF
vectorizer = TfidfVectorizer(max_features=3000)
x = vectorizer.fit_transform(df["clean_text"])
y = df["label"]

# Train Test Split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

# Train Model
model = MultinomialNB()
model.fit(x_train, y_train)

# Evaluation
y_pred = model.predict(x_test)
print(f"\nAccuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Predict Email Function
def predict_email(email_text):
    processed_text = preprocess_text(email_text)
    vectorized_text = vectorizer.transform([processed_text])
    prediction = model.predict(vectorized_text)
    return "Spam" if prediction[0] == 1 else "Not Spam"

# Testing Examples
print("\n=== Testing Predictions ===")
test_emails = [
    "Congratulations! You've won a free iphone. Click here to claim now",
    "Hey are we still meeting for lunch today at 12?",
    "URGENT: Your account will be closed. Verify your login now at http://fake.com"
]

for mail in test_emails:
    print(f"Email     : {mail}")
    print(f"Prediction: {predict_email(mail)}\n")
