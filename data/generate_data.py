"""
Professional Pakistani Used Car Market Dataset Generator
Includes Toyota, Honda, Suzuki, KIA, Hyundai, Changan, MG, Haval, Daihatsu
Features: Brand, Model, Year, Mileage, Engine CC, Transmission, Fuel, Assembly, Body Condition, Registered City, and realistic PKR Prices.
"""

import numpy as np
import pandas as pd
import random
import os

CAR_SPECS = [
    # Suzuki
    {"brand": "Suzuki", "model_name": "Alto", "base_price": 2700000, "engine_cc": 660, "transmissions": ["Manual", "Automatic"], "fuel": "Petrol", "assembly": "Local"},
    {"brand": "Suzuki", "model_name": "Cultus", "base_price": 3900000, "engine_cc": 1000, "transmissions": ["Manual", "Automatic"], "fuel": "Petrol", "assembly": "Local"},
    {"brand": "Suzuki", "model_name": "WagonR", "base_price": 3300000, "engine_cc": 1000, "transmissions": ["Manual", "Automatic"], "fuel": "Petrol", "assembly": "Local"},
    {"brand": "Suzuki", "model_name": "Swift", "base_price": 4600000, "engine_cc": 1200, "transmissions": ["Automatic", "Manual"], "fuel": "Petrol", "assembly": "Local"},
    {"brand": "Suzuki", "model_name": "Mehran", "base_price": 1400000, "engine_cc": 800, "transmissions": ["Manual"], "fuel": "Petrol", "assembly": "Local"},

    # Toyota
    {"brand": "Toyota", "model_name": "Corolla Altis", "base_price": 6300000, "engine_cc": 1600, "transmissions": ["Automatic", "Manual"], "fuel": "Petrol", "assembly": "Local"},
    {"brand": "Toyota", "model_name": "Corolla Grande", "base_price": 7600000, "engine_cc": 1800, "transmissions": ["Automatic"], "fuel": "Petrol", "assembly": "Local"},
    {"brand": "Toyota", "model_name": "Yaris", "base_price": 4800000, "engine_cc": 1300, "transmissions": ["Automatic", "Manual"], "fuel": "Petrol", "assembly": "Local"},
    {"brand": "Toyota", "model_name": "Fortuner", "base_price": 18500000, "engine_cc": 2800, "transmissions": ["Automatic"], "fuel": "Diesel", "assembly": "Local"},
    {"brand": "Toyota", "model_name": "Hilux Revo", "base_price": 14500000, "engine_cc": 2800, "transmissions": ["Automatic"], "fuel": "Diesel", "assembly": "Local"},
    {"brand": "Toyota", "model_name": "Aqua", "base_price": 5400000, "engine_cc": 1500, "transmissions": ["Automatic"], "fuel": "Hybrid", "assembly": "Imported"},
    {"brand": "Toyota", "model_name": "Prius", "base_price": 7800000, "engine_cc": 1800, "transmissions": ["Automatic"], "fuel": "Hybrid", "assembly": "Imported"},
    {"brand": "Toyota", "model_name": "Prado", "base_price": 32000000, "engine_cc": 3000, "transmissions": ["Automatic"], "fuel": "Diesel", "assembly": "Imported"},

    # Honda
    {"brand": "Honda", "model_name": "Civic Oriel", "base_price": 8600000, "engine_cc": 1500, "transmissions": ["Automatic"], "fuel": "Petrol", "assembly": "Local"},
    {"brand": "Honda", "model_name": "Civic RS Turbo", "base_price": 9900000, "engine_cc": 1500, "transmissions": ["Automatic"], "fuel": "Petrol", "assembly": "Local"},
    {"brand": "Honda", "model_name": "City Aspire", "base_price": 5400000, "engine_cc": 1500, "transmissions": ["Automatic", "Manual"], "fuel": "Petrol", "assembly": "Local"},
    {"brand": "Honda", "model_name": "City 1.2", "base_price": 4600000, "engine_cc": 1200, "transmissions": ["Manual", "Automatic"], "fuel": "Petrol", "assembly": "Local"},
    {"brand": "Honda", "model_name": "Vezel", "base_price": 7200000, "engine_cc": 1500, "transmissions": ["Automatic"], "fuel": "Hybrid", "assembly": "Imported"},
    {"brand": "Honda", "model_name": "BR-V", "base_price": 6200000, "engine_cc": 1500, "transmissions": ["Automatic"], "fuel": "Petrol", "assembly": "Local"},

    # KIA
    {"brand": "KIA", "model_name": "Sportage", "base_price": 7800000, "engine_cc": 2000, "transmissions": ["Automatic"], "fuel": "Petrol", "assembly": "Local"},
    {"brand": "KIA", "model_name": "Picanto", "base_price": 3600000, "engine_cc": 1000, "transmissions": ["Automatic", "Manual"], "fuel": "Petrol", "assembly": "Local"},
    {"brand": "KIA", "model_name": "Stonic", "base_price": 5300000, "engine_cc": 1400, "transmissions": ["Automatic"], "fuel": "Petrol", "assembly": "Local"},

    # Hyundai
    {"brand": "Hyundai", "model_name": "Tucson", "base_price": 8400000, "engine_cc": 2000, "transmissions": ["Automatic"], "fuel": "Petrol", "assembly": "Local"},
    {"brand": "Hyundai", "model_name": "Elantra", "base_price": 6800000, "engine_cc": 2000, "transmissions": ["Automatic"], "fuel": "Petrol", "assembly": "Local"},
    {"brand": "Hyundai", "model_name": "Sonata", "base_price": 11200000, "engine_cc": 2500, "transmissions": ["Automatic"], "fuel": "Petrol", "assembly": "Local"},

    # Changan
    {"brand": "Changan", "model_name": "Alsvin", "base_price": 4400000, "engine_cc": 1500, "transmissions": ["Automatic", "Manual"], "fuel": "Petrol", "assembly": "Local"},
    {"brand": "Changan", "model_name": "Oshan X7", "base_price": 8900000, "engine_cc": 1500, "transmissions": ["Automatic"], "fuel": "Petrol", "assembly": "Local"},

    # MG
    {"brand": "MG", "model_name": "MG HS", "base_price": 8200000, "engine_cc": 1500, "transmissions": ["Automatic"], "fuel": "Petrol", "assembly": "Local"},
    {"brand": "MG", "model_name": "MG ZS", "base_price": 5400000, "engine_cc": 1500, "transmissions": ["Automatic"], "fuel": "Petrol", "assembly": "Local"},

    # Haval
    {"brand": "Haval", "model_name": "Haval H6", "base_price": 11800000, "engine_cc": 2000, "transmissions": ["Automatic"], "fuel": "Hybrid", "assembly": "Local"},

    # Daihatsu
    {"brand": "Daihatsu", "model_name": "Mira", "base_price": 3400000, "engine_cc": 660, "transmissions": ["Automatic"], "fuel": "Petrol", "assembly": "Imported"}
]

def generate_pro_dataset(n_samples=6000, seed=42):
    np.random.seed(seed)
    random.seed(seed)
    current_year = 2024
    records = []

    for _ in range(n_samples):
        spec = random.choice(CAR_SPECS)
        brand = spec["brand"]
        model = spec["model_name"]
        engine_cc = spec["engine_cc"]
        fuel = spec["fuel"]
        assembly = spec["assembly"]
        transmission = random.choice(spec["transmissions"])

        # Year distribution: Mehran/Prado can be older, others 2012-2024
        if model == "Mehran":
            year = int(np.random.randint(2010, 2019))
        elif model == "Prado":
            year = int(np.random.randint(2008, 2024))
        else:
            year = int(np.random.randint(2014, 2025))

        age = current_year - year

        # Mileage: 10,000 to 20,000 km per year
        avg_km_year = np.random.uniform(9000, 17000)
        mileage_km = int(max(age * avg_km_year + np.random.normal(0, 7000), 4000))
        mileage_km = min(mileage_km, 300000)

        # Professional Attributes
        # 1. Registered City
        reg_city = np.random.choice(["Islamabad", "Lahore", "Karachi", "Other"], p=[0.35, 0.35, 0.20, 0.10])

        # 2. Body Condition / Paint
        body_condition = np.random.choice(["100% Genuine", "Minor Touchups", "Accidental / Repainted"], p=[0.45, 0.40, 0.15])

        # Base price calculations
        base = spec["base_price"]

        # Depreciation per year: ~6.2%
        price = base * ((1 - 0.062) ** age)

        # Mileage adjustment: -0.25% per 10,000 km
        mileage_penalty = (mileage_km / 10000) * 0.0025 * base
        price -= mileage_penalty

        # Automatic transmission bump
        if transmission == "Automatic":
            price += base * 0.035

        # Registration City Adjustment
        if reg_city == "Islamabad":
            price += base * 0.03  # Islamabad registered cars have higher demand
        elif reg_city == "Karachi":
            price -= base * 0.02  # Karachi cars often have rust discount

        # Body Condition Adjustment
        if body_condition == "100% Genuine":
            price += base * 0.04  # Mint condition premium
        elif body_condition == "Accidental / Repainted":
            price -= base * 0.18  # Substantial hit for repainted cars

        # Small market randomness (±2%)
        noise = np.random.normal(0, base * 0.02)
        final_price = round(price + noise, -4)

        # Floor price
        final_price = max(final_price, 750000)

        records.append({
            "brand": brand,
            "model_name": model,
            "model_year": year,
            "engine_cc": engine_cc,
            "transmission": transmission,
            "fuel_type": fuel,
            "assembly": assembly,
            "registered_city": reg_city,
            "body_condition": body_condition,
            "mileage_km": mileage_km,
            "price_pkr": int(final_price)
        })

    return pd.DataFrame(records)

if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(out_dir, "car_data.csv")
    df = generate_pro_dataset(6000)
    df.to_csv(csv_path, index=False)
    print(f"Generated {len(df)} professional car records across {df['brand'].nunique()} brands and {df['model_name'].nunique()} models at {csv_path}")
