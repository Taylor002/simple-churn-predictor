import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Sample dataset (You can replace with real data)
data = {
    'Tenure': [12, 3, 24, 6, 5, 18],
    'Balance': [5000, 1000, 7000, 2000, 1500, 6500],
    'Transactions': [45, 10, 60, 15, 8, 50],
    'Complaints': [0, 2, 1, 1, 3, 0],
    'Churn': [0, 1, 0, 1, 1, 0]
}
df = pd.DataFrame(data)

X = df[['Tenure', 'Balance', 'Transactions', 'Complaints']]
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
