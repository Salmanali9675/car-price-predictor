"""
Car Valuation & Market Intelligence Engine
Encapsulates inference, feature alignment, price-range calculation, and inspection ratings.
"""

import os
import joblib
import pandas as pd

class CarEvaluator:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.model_path = os.path.join(base_dir, 'model', 'car_price_model.joblib')
        self.columns_path = os.path.join(base_dir, 'model', 'feature_columns.joblib')
        self.model = None
        self.feature_columns = None
        self._load_artifacts()

    def _load_artifacts(self):
        if os.path.exists(self.model_path) and os.path.exists(self.columns_path):
            self.model = joblib.load(self.model_path)
            self.feature_columns = joblib.load(self.columns_path)
        else:
            raise FileNotFoundError("Model artifacts not found. Run model/train.py first.")

    def evaluate(self, specs):
        """
        Takes vehicle specifications dict and returns a comprehensive valuation report.
        """
        brand = specs.get('brand', 'Toyota')
        model_name = specs.get('model_name', 'Corolla Altis')
        model_year = int(specs.get('model_year', 2020))
        engine_cc = int(specs.get('engine_cc', 1600))
        transmission = specs.get('transmission', 'Automatic')
        fuel_type = specs.get('fuel_type', 'Petrol')
        assembly = specs.get('assembly', 'Local')
        reg_city = specs.get('registered_city', 'Islamabad')
        body_condition = specs.get('body_condition', '100% Genuine')
        mileage_km = int(specs.get('mileage_km', 45000))

        # Build feature vector matching the trained columns
        row_dict = {col: [0] for col in self.feature_columns}
        input_df = pd.DataFrame(row_dict)

        # Numerical assignments
        if 'model_year' in input_df.columns:
            input_df['model_year'] = [model_year]
        if 'engine_cc' in input_df.columns:
            input_df['engine_cc'] = [engine_cc]
        if 'mileage_km' in input_df.columns:
            input_df['mileage_km'] = [mileage_km]

        # Categorical switches
        switches = [
            f"brand_{brand}",
            f"model_name_{model_name}",
            f"transmission_{transmission}",
            f"fuel_type_{fuel_type}",
            f"assembly_{assembly}",
            f"registered_city_{reg_city}",
            f"body_condition_{body_condition}"
        ]

        for s in switches:
            if s in input_df.columns:
                input_df[s] = [1]

        # Model inference
        predicted_price = float(self.model.predict(input_df)[0])
        lakhs = predicted_price / 100000.0
        crores = predicted_price / 10000000.0

        # Market Ranges
        fair_range_low = round(predicted_price * 0.96, -4)
        fair_range_high = round(predicted_price * 1.04, -4)
        dealer_cash = round(predicted_price * 0.92, -4)

        # Inspection score out of 10.0
        score = 9.8
        if body_condition == "Minor Touchups":
            score -= 1.2
        elif body_condition == "Accidental / Repainted":
            score -= 3.0
        age = 2024 - model_year
        score -= min(age * 0.2, 2.0)
        score = max(round(score, 1), 3.5)

        return {
            'predicted_price': int(predicted_price),
            'price_lakhs': round(lakhs, 2),
            'price_crores': round(crores, 2),
            'price_display': f"{crores:.2f} Crore PKR" if crores >= 1.0 else f"{lakhs:.2f} Lakh PKR",
            'fair_range_low': int(fair_range_low),
            'fair_range_high': int(fair_range_high),
            'dealer_cash': int(dealer_cash),
            'inspection_score': score,
            'reg_city': reg_city,
            'body_condition': body_condition
        }
