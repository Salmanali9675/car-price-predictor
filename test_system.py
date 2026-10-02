"""
Automated 5-Point Verification Suite for PakWheels Car Price Evaluator
"""

import sys
import os

# Add root to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.car_evaluator import CarEvaluator

def run_tests():
    print("=== Starting PakWheels Car Evaluator Verification Suite ===")
    evaluator = CarEvaluator()

    # Test 1: Budget Small Car (Suzuki Alto 2020)
    print("\n[Test 1] Budget Category Valuation: Suzuki Alto 2020...")
    alto_specs = {
        'brand': 'Suzuki',
        'model_name': 'Alto',
        'model_year': 2020,
        'engine_cc': 660,
        'transmission': 'Automatic',
        'fuel_type': 'Petrol',
        'assembly': 'Local',
        'registered_city': 'Islamabad',
        'body_condition': '100% Genuine',
        'mileage_km': 45000
    }
    res1 = evaluator.evaluate(alto_specs)
    print(f"Price: Rs. {res1['predicted_price']:,} ({res1['price_display']}) | Score: {res1['inspection_score']}/10")
    assert 2000000 <= res1['predicted_price'] <= 2600000, f"Alto price out of expected range: {res1['predicted_price']}"
    print("[PASS] Test 1 Passed: Alto valuation is accurate within market baseline (20L - 26L)!")

    # Test 2: Luxury SUV (Toyota Fortuner 2022)
    print("\n[Test 2] Luxury SUV Category: Toyota Fortuner 2022...")
    fortuner_specs = {
        'brand': 'Toyota',
        'model_name': 'Fortuner',
        'model_year': 2022,
        'engine_cc': 2800,
        'transmission': 'Automatic',
        'fuel_type': 'Diesel',
        'assembly': 'Local',
        'registered_city': 'Islamabad',
        'body_condition': '100% Genuine',
        'mileage_km': 30000
    }
    res2 = evaluator.evaluate(fortuner_specs)
    print(f"Price: Rs. {res2['predicted_price']:,} ({res2['price_display']}) | Score: {res2['inspection_score']}/10")
    assert 14000000 <= res2['predicted_price'] <= 18000000, f"Fortuner price out of expected range: {res2['predicted_price']}"
    print("[PASS] Test 2 Passed: Fortuner valuation accurate within luxury market baseline (1.4Cr - 1.8Cr)!")

    # Test 3: Mileage Impact (Low vs High Mileage)
    print("\n[Test 3] Mileage Depreciation Verification...")
    low_km_specs = dict(alto_specs, mileage_km=15000)
    high_km_specs = dict(alto_specs, mileage_km=160000)
    p_low = evaluator.evaluate(low_km_specs)['predicted_price']
    p_high = evaluator.evaluate(high_km_specs)['predicted_price']
    diff = p_low - p_high
    print(f"Low Mileage (15,000 km) : Rs. {p_low:,}")
    print(f"High Mileage (160,000 km): Rs. {p_high:,}")
    print(f"Depreciation Deduction  : Rs. {diff:,}")
    assert p_low > p_high, "Low mileage car must be priced higher than high mileage car"
    print("[PASS] Test 3 Passed: Mileage negative correlation confirmed!")

    # Test 4: Body Condition Impact (Genuine vs Accidental)
    print("\n[Test 4] Body Condition Impact (100% Genuine vs Accidental)...")
    genuine_specs = dict(alto_specs, body_condition='100% Genuine')
    accidental_specs = dict(alto_specs, body_condition='Accidental / Repainted')
    p_genuine = evaluator.evaluate(genuine_specs)['predicted_price']
    p_accidental = evaluator.evaluate(accidental_specs)['predicted_price']
    discount = p_genuine - p_accidental
    print(f"100% Genuine : Rs. {p_genuine:,}")
    print(f"Accidental   : Rs. {p_accidental:,}")
    print(f"Damage Cut   : Rs. {discount:,}")
    assert p_genuine > p_accidental, "Genuine body must carry higher value than accidental"
    print("[PASS] Test 4 Passed: Accidental damage penalty correctly applied!")

    # Test 5: Registration City Premium (Islamabad vs Karachi)
    print("\n[Test 5] Regional Jurisdiction Premium (Islamabad vs Karachi)...")
    isb_specs = dict(alto_specs, registered_city='Islamabad')
    khi_specs = dict(alto_specs, registered_city='Karachi')
    p_isb = evaluator.evaluate(isb_specs)['predicted_price']
    p_khi = evaluator.evaluate(khi_specs)['predicted_price']
    print(f"Islamabad Registered: Rs. {p_isb:,}")
    print(f"Karachi Registered  : Rs. {p_khi:,}")
    assert p_isb > p_khi, "Islamabad registered vehicle must carry liquidity premium over Karachi"
    print("[PASS] Test 5 Passed: Regional registration dynamics operational!")

    print("\n=======================================================")
    print(" ALL 5 AUTOMATED VERIFICATION TESTS PASSED SUCCESSFULLY!")
    print("=======================================================")

if __name__ == '__main__':
    run_tests()
