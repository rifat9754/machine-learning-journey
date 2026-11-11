# Linear, Ridge & Lasso Regression

A Machine Learning project comparing Linear Regression, Ridge Regression, and Lasso Regression using the Boston Housing Dataset.

## Overview

This project explores how regularization techniques improve Linear Regression and helps understand the differences between Ridge and Lasso Regression.

## Dataset

**Boston Housing Dataset**

- Samples: 506
- Features: 13
- Target: MEDV (Median House Value)
- Source: OpenML

## Technologies

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

## Algorithms Implemented

1. Linear Regression
2. Ridge Regression (L2 Regularization)
3. Lasso Regression (L1 Regularization)

## Concepts Covered

- Data Loading and Preprocessing
- Independent and Dependent Features
- Train-Test Split
- Feature Scaling (StandardScaler)
- Cross-Validation
- Hyperparameter Tuning using GridSearchCV
- Regularization (L1 and L2)
- Model Prediction
- Model Evaluation

## Model Evaluation

The models are evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

## Implementation

- Linear Regression baseline model
- Ridge Regression with different alpha values
- Lasso Regression with different alpha values
- Hyperparameter selection using 5-fold cross-validation
- Comparison of model performance using R² Score

## Goal

To understand how Ridge and Lasso regularization work, how they control model complexity, and how they differ from ordinary Linear Regression.

## Note

The Boston Housing Dataset is a historical educational dataset with known ethical limitations. It should not be used for real-world housing valuation or consequential decision-making.