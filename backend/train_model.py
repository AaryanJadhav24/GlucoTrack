# train_model.py

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

# Load the dataset
df = pd.read_csv("diabetes.csv")

# Remove rows with zero in important features (likely missing)
df = df[(df[['Glucose', 'BMI', 'Insulin', 'BloodPressure']] != 0).all(axis=1)]

# Define features and target
X = df.drop(columns=['Outcome', 'Glucose'])  # Predict glucose, don't include outcome
y = df['Glucose']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
mse = mean_squared_error(y_test, preds)
print(f"Model trained. MSE: {mse:.2f}")

# Save the model
joblib.dump(model, "glucose_predictor.pkl")
print("Model saved as glucose_predictor.pkl")
