"""
Retrain Random Forest Regressor on the 6,000 Professional Used Car Dataset
"""

import pandas as pd
import numpy as np
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, 'data', 'car_data.csv')
model_dir = os.path.join(BASE_DIR, 'model')

print(f"Loading data from {data_path}...")
df = pd.read_csv(data_path)

# One-hot encode categorical columns
df_encoded = pd.get_dummies(df, drop_first=True)

# Separate features (X) and target (y)
X = df_encoded.drop('price_pkr', axis=1)
y = df_encoded['price_pkr']

# Train/Test Split (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Train size: {X_train.shape[0]}, Test size: {X_test.shape[0]}, Features: {X.shape[1]}")

# Train Random Forest
print("Training Random Forest Regressor on 31 car models...")
rf = RandomForestRegressor(n_estimators=120, max_depth=20, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)

# Evaluate
preds = rf.predict(X_test)
mae = mean_absolute_error(y_test, preds)
r2 = r2_score(y_test, preds)

print(f"\n--- Model Evaluation ---")
print(f"R² Score: {r2 * 100:.2f}%")
print(f"MAE: Rs. {mae:,.0f}")

# Save artifacts
model_path = os.path.join(model_dir, 'car_price_model.joblib')
cols_path = os.path.join(model_dir, 'feature_columns.joblib')

joblib.dump(rf, model_path)
joblib.dump(list(X.columns), cols_path)

print(f"Successfully saved model to {model_path}")
print(f"Successfully saved feature columns to {cols_path}")
