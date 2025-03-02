#models/train_model.py
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline

# Load dataset
import pandas as pd

df = pd.read_csv("dataset/cplusplus_bugs.csv", delimiter=",", encoding="utf-8", on_bad_lines='skip')

# Features (C++ code) and labels (bug types)
X = df["Code Snippet"]
y = df["Bug Type"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Transform text into numerical features-
X_train_features = vectorizer.fit_transform(X_train)
X_test_features = vectorizer.transform(X_test)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_features, y_train)

# Save vectorizer and model
joblib.dump(vectorizer, "models/vectorizer.pkl")
joblib.dump(model, "models/model.pkl")

print("✅ Model and vectorizer trained & saved in models/ directory.")
