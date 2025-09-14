# Simple Churn Predictor

🚀 A beginner-friendly AI project that predicts customer churn based on basic features.

## Features
- Upload CSV with `Tenure, Balance, Transactions, Complaints`
- Logistic Regression model predicts churn (0 = Stay, 1 = Leave)
- Results displayed in a clean HTML table

## How to Run
1. Clone the repo
2. Install requirements:
   ```
   pip install -r requirements.txt
   ```
3. Train model:
   ```
   python train_model.py
   ```
4. Run app:
   ```
   python app.py
   ```
5. Open browser at `http://127.0.0.1:5000`

## Example Input
```csv
Tenure,Balance,Transactions,Complaints
12,5000,45,0
3,1000,10,2
```

## Roadmap
- Add more ML models
- Add visualization (charts)
- Deploy on cloud
- API endpoint for predictions
