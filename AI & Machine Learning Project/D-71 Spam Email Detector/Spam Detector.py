import os
import pandas as pd 
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# Download NLTK data
nltk.download("stopwords", quiet=True)
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))


# Load dataset
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
print("Preprocessed Data:")
print(df[["label", "clean_text"]].head())

# Feature Extraction with TF-IDF
vectorizer = TfidfVectorizer(max_features=3000)
x = vectorizer.fit_transform(df["clean_text"])
y = df["label"]

# Train Test Split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train Model
model = LogisticRegression()
model.fit(x_train, y_train)

# Evaluation
y_pred = model.predict(x_test)
print(f"\nAccuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Prediction Function
def predict_email(email_text):
    processed_text = preprocess_text(email_text)
    vectorized_text = vectorizer.transform([processed_text])
    prediction = model.predict(vectorized_text)
    return "Spam" if prediction[0] == 1 else "Not Spam (Ham)"

# Example Testing
email = "Congratulations! You've won a free iPhone. Click here to claim now"
print(f"\nEmail: {email}")
print(f"Prediction: {predict_email(email)}")
