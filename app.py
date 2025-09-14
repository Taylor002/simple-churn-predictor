from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["file"]
    if not file:
        return "No file uploaded!"

    df = pd.read_csv(file)

    X = df[['Tenure', 'Balance', 'Transactions', 'Complaints']]
    preds = model.predict(X)
    df["Predicted_Churn"] = preds

    result_html = df.to_html(classes="table table-striped", index=False)
    return f"<h2>Prediction Results</h2>{result_html}<br><a href='/'>Back</a>"

if __name__ == "__main__":
    app.run(debug=True)
