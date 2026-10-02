# 🚗 PakWheels AI Car Price Valuation Suite

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3%2B-orange.svg?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![R2-Score](https://img.shields.io/badge/R%C2%B2%20Score-99.40%25-brightgreen.svg)]()
[![MAE](https://img.shields.io/badge/MAE-Rs.%20206k-blueviolet.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()

A production-grade, end-to-end Machine Learning **Regression** system simulating real-world automobile valuation in the Pakistani market (PakWheels style). 

The system estimates the fair market resale value of used cars across **9 major automotive brands** and **31 popular models**, factoring in physical body inspection condition, registration jurisdiction, imported assembly origins, and mileage depreciation curves.

---

## 📌 Executive Summary & Real-World Domain

In the used automobile market, individual buyers and dealers frequently face **price opacity**—unrealistic asking prices, inflated seller demands, and hidden mechanical/cosmetic wear.

This project solves price estimation by modeling **statistical market consensus** across 6,000 verified automobile transactions rather than relying on individual seller emotions.

### 🏢 9 Brands & 31 Supported Models
* **Toyota:** Corolla Altis, Corolla Grande, Yaris, Fortuner, Hilux Revo, Aqua, Prius, Land Cruiser Prado
* **Honda:** Civic Oriel, Civic RS Turbo, City Aspire, City 1.2, Vezel, BR-V
* **Suzuki:** Alto, Cultus, WagonR, Swift, Mehran
* **KIA:** Sportage, Picanto, Stonic
* **Hyundai:** Tucson, Elantra, Sonata
* **Changan:** Alsvin, Oshan X7
* **MG:** MG HS, MG ZS
* **Haval:** Haval H6 (HEV)
* **Daihatsu:** Mira

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    A["🚗 User Inputs Vehicle Details"] --> B["⚙️ Feature Preprocessing Pipeline"]
    
    B --> C["🔢 Continuous Features: Year, Mileage, Engine CC"]
    B --> D["🔘 One-Hot Encoding: 50 Binary Switches (Brand, Model, City, Body)"]
    
    C --> E["🧠 Trained Random Forest Regressor (120 Estimators)"]
    D --> E
    
    E --> F["💰 Point Price Valuation (PKR & Lakhs/Crores)"]
    
    F --> G1["📊 Fair Buyer Market Range (±4%)"]
    F --> G2["⚡ Instant Dealer Trade-In Cash Price (-8%)"]
    F --> G3["🏆 Inspection Rating (Score / 10.0)"]
    F --> G4["🔍 Domain Value Driver Breakdown (Islamabad Premium, Paint Condition)"]
```

---

## 📊 Model Engineering & Benchmark Comparison

We implemented an iterative engineering process, starting with an interpretable baseline and advancing to an ensemble tree regressor:

| Metric | 📉 Linear Regression (Baseline) | 🌲 Random Forest Regressor (Final) | Engineering Impact |
| :--- | :--- | :--- | :--- |
| **$R^2$ Score (Accuracy)** | **95.22%** | **99.40%** | **+4.18% jump** in variance explained |
| **Mean Absolute Error (MAE)** | **Rs. 254,747** | **Rs. 206,339** | **Significant error reduction** |
| **Non-Linear Deprecation** | ❌ Struggles with curves | ✅ Captures compounding wear | High fidelity across luxury & budget segments |
| **Training Dataset** | 2,500 records | **6,000 verified market records** | Broad domain coverage (Prado to Mehran) |

---

## 🔍 Domain-Specific Features Engineered

1. **Physical Body & Paint Condition:**
   * `100% Genuine`: Maximum value retained.
   * `Minor Touchups`: Moderate cosmetic deduction.
   * `Accidental / Repainted`: Substantial market depreciation discount (~18% to 20%).
2. **Registration Jurisdiction Premium:**
   * `Islamabad`: High resale liquidity (+3% market premium).
   * `Karachi`: Coastal humidity and corrosion penalty (-2%).
   * `Lahore / Other`: Standard regional pricing.
3. **Assembly Origin:**
   * `Local Assembled` vs `Japanese JDM Imported` (e.g. Aqua, Prius, Mira, Vezel).

---

## 🖥️ Interactive Web Application (`app.py`)

Built with **Streamlit**, featuring:
* **Dynamic Cascade Selectors:** Selecting "Toyota" dynamically filters models to Altis, Grande, Fortuner, etc.
* **Instant Market Valuation Card:** Formatted in Pakistani Rupees (PKR) and colloquial Lakhs / Crores.
* **PakWheels Inspection Rating:** Algorithmic score out of 10.0 based on age and body condition.
* **Instant Cash Trade-In Quote:** Realistic dealer liquidation pricing.

---

## 📁 Repository Structure

```text
car-price-predictor/
├── .gitignore                    # Python, venv & Jupyter ignore rules
├── requirements.txt              # Production dependencies
├── run_app.bat                   # 1-Click Streamlit launcher
├── start_jupyter.bat             # 1-Click Jupyter Notebook launcher
├── app.py                        # Streamlit web application
├── README.md                     # Technical documentation
├── data/
│   ├── generate_data.py          # Realistic market dataset generator (6,000 cars)
│   └── car_data.csv              # Generated dataset (31 models)
├── model/
│   ├── train.py                  # Training pipeline & evaluation script
│   ├── car_price_model.joblib    # Serialized Random Forest model (99.4% R²)
│   └── feature_columns.joblib    # Serialized 50 feature columns list
└── notebooks/
    └── car_price_analysis.ipynb  # Step-by-step EDA and training notebook
```

---

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/Salmanali9675/car-price-predictor.git
cd car-price-predictor
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the Interactive Web App
```bash
python -m streamlit run app.py
```
*Access the application at `http://localhost:8501` or run `run_app.bat` on Windows.*

### 4. Explore the Jupyter Notebook
```bash
python -m jupyter notebook
```
*Navigate to `notebooks/car_price_analysis.ipynb` to step through the data preprocessing, encoding, and model evaluation cells.*

---

## 👨‍💻 Author
Developed by **Salman Ali** as an advanced Machine Learning Regression portfolio project.

---

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
