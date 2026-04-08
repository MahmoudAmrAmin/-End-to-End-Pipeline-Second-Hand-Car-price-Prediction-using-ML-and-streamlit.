# 🚗 Second Hand Car Price Prediction

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.56.0-FF4B4B.svg)
![CatBoost](https://img.shields.io/badge/CatBoost-1.2.10-yellow.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Regression-brightgreen)

An end-to-end Machine Learning web application designed to estimate the market value of used cars. Built with a modern **Streamlit** user interface, this project leverages a robust data science pipeline—from extensive exploratory data analysis (EDA) to advanced model training utilizing **CatBoost**.

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Project Structure](#-project-structure)
- [Methodology & Approaches](#-methodology--approaches)
- [Technologies Used](#-technologies-used)
- [Installation & Usage](#-installation--usage)
- [Copyright & License](#-copyright--license)

---

## 📖 Overview
Predicting the price of a second-hand car is a complex regression problem that depends on multiple factors such as brand value, mileage, manufacturing year, and engine specifications. This project provides a highly accurate predictive model wrapped in an interactive, user-friendly web interface. 

Users simply input the car's specifications, and the application applies pre-trained scalers and encoders to feed the data into a machine learning model, returning an instant, data-driven market estimate.

---

## 🗂️ Project Structure
The repository follows a standard, modular data science lifecycle structure:

```text
├── data/
│   └── raw_data.xlsx               # Raw dataset containing car listings
├── models/
│   ├── Model.pkl                   # Trained regression model (CatBoost)
│   ├── Brand_Encoder.pkl           # Target encoder mapping for Car Brands
│   ├── Model_Encoder.pkl           # Target encoder mapping for Car Models
│   └── OHE_Encoder.pkl             # One-Hot Encoder for categorical features
├── src/
│   ├── 1-cleaning/                 # Jupyter notebooks for data wrangling
│   ├── 2-eda/                      # Exploratory Data Analysis & Visualization
│   ├── 3-preprocessing/            # Feature engineering and encoding
│   ├── 4-splitting/                # Train/test split strategies
│   └── 5-modelling/                # Model training, hyperparameter tuning & evaluation
├── app.py                          # Main Streamlit web application
├── requirements.txt                # Project dependencies
└── README.md                       # Project documentation
🔬 Methodology & Approaches
This project was built using a structured machine learning pipeline:

Data Cleaning & Wrangling (1-cleaning)

Handled missing values and outliers.

Standardized data types and corrected structural errors in the dataset.

Exploratory Data Analysis (2-eda)

Utilized Plotly, Seaborn, and Matplotlib to discover patterns and correlations.

Analyzed price distributions across different brands, fuel types, and transmission types.

Data Preprocessing & Feature Engineering (3-preprocessing)

Target Encoding: Applied to high-cardinality categorical variables (Brand and Model) to capture the mean target value associated with each category without exploding the feature space.

One-Hot Encoding (OHE): Applied to low-cardinality nominal features (Fuel and Transmission).

Managed unseen categories gracefully using mean imputation fallbacks.

Modeling & Evaluation (5-modelling)

Tested multiple gradient boosting frameworks (including XGBoost and CatBoost).

Selected CatBoost as the final model due to its robust performance on datasets with heavy categorical features and its resistance to overfitting.

💻 Technologies Used
Core: Python, Pandas, NumPy

Machine Learning: Scikit-Learn, CatBoost, XGBoost

Data Visualization: Plotly, Seaborn, Matplotlib

Web App & UI: Streamlit (with Custom CSS for a dark-mode, modern UI)

Serialization: Pickle

🚀 Installation & Usage
To run this project locally, follow these steps:

1. Clone the repository
Bash
git clone [https://github.com/yourusername/second-hand-car-price-prediction.git](https://github.com/yourusername/second-hand-car-price-prediction.git)
cd second-hand-car-price-prediction
2. Set up a virtual environment (Recommended)
Bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. Install dependencies
Bash
pip install -r requirements.txt
4. Run the Streamlit Application
Bash
streamlit run app.py
The application will automatically open in your default web browser at http://localhost:8501.

©️ Copyright & License
© 2026 Mahmoud. All rights reserved.

This project, including its source code, models, data processing pipelines, and user interface design, is the intellectual property of Mahmoud, AI & Machine Learning Engineer.

Unauthorized copying, modification, distribution, or commercial use of this repository, via any medium, is strictly prohibited without explicit written permission from the author.

If you would like to use or adapt portions of this codebase for academic or non-commercial purposes, please reach out for permission and ensure proper attribution.
