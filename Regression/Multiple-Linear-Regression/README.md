# Multiple Linear Regression – House Price Prediction

A machine learning project that predicts house prices using Multiple Linear Regression.

## Project Overview

This project implements Multiple Linear Regression using two approaches:

- NumPy: Gradient Descent from scratch
- Scikit-learn: LinearRegression

The model predicts house prices based on multiple property features.

## Dataset

This project uses a synthetically generated dataset containing 500 records.

| Feature | Description |
|---|---|
| Area | House area in square feet |
| Bedrooms | Number of bedrooms |
| Bathrooms | Number of bathrooms |
| Age | Age of the house |
| Location_Score | Location quality score |
| Price | House price in lakh BDT (target) |

**Note:** The dataset is synthetic and intended for learning purposes, not real-world property valuation.

## Project Structure

```text
Multiple-Linear-Regression/
├── data/
│   └── house_prices.csv
├── images/
├── models/
│   ├── multiple_linear_regression.pkl
│   ├── feature_scaler.pkl
│   └── custom_multiple_linear_regression.pkl
├── src/
│   └── multiple_linear_regression.py
├── Multiple_Linear_Regression.ipynb
├── README.md
└── requirements.txt
```

## Concepts Covered

- Multiple Linear Regression
- Exploratory Data Analysis (EDA)
- Correlation Analysis
- Multicollinearity and VIF
- Train-Test Split
- Feature Scaling
- Gradient Descent from scratch
- Scikit-learn implementation
- Model Evaluation
- Residual Analysis
- Model Serialization using Joblib

## Evaluation Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

## Installation

```bash
git clone https://github.com/rifat9754/machine-learning-journey.git
cd machine-learning-journey/Regression/Multiple-Linear-Regression
pip install -r requirements.txt
jupyter notebook
```

## Learning Outcomes

After completing this project, I learned how multiple independent variables influence a target variable, how to implement Gradient Descent from scratch, and how to train, evaluate, and save a regression model.