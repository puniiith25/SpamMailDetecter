import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Example dataset
data = {
    "text": [
        "Win money now",
        "Congratulations you won lottery",
        "Claim your free prize",
        "Earn cash fast",
        "Hello how are you",
        "Let's meet tomorrow",
        "Project meeting at 5pm",
        "Can we discuss assignment",
        "Free iphone offer click here",
        "Limited time offer"
    ],
    "label": [1,1,1,1,0,0,0,0,1,1]  # 1 = Spam, 0 = Not Spam
}

df = pd.DataFrame(data)

X = df["text"]
y = df["label"]

vectorizer = TfidfVectorizer()
X_vector = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vector, y)

# Save model
pickle.dump(model, open("spam_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
print("Model and Vectorizer saved")