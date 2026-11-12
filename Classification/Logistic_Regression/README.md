# Logistic Regression – Breast Cancer Classification

A Machine Learning project that uses Logistic Regression to classify breast cancer tumors as malignant or benign.

## Overview

This project implements Logistic Regression using Scikit-learn and the Breast Cancer dataset. The goal is to predict whether a tumor is malignant or benign based on the input features.

## Dataset

**Breast Cancer Wisconsin Dataset**

- **Source:** Scikit-learn built-in dataset
- **Total Samples:** 569
- **Features:** 30
- **Target:** Cancer classification
- **Classes:**
  - `0` – Malignant
  - `1` – Benign

## Technologies

- Python
- Pandas
- Scikit-learn
- Matplotlib

## Algorithm Implemented

1. Logistic Regression

## Concepts Covered

- Dataset Loading
- Feature and Target Separation
- Train-Test Split
- Feature Scaling using StandardScaler
- Logistic Regression Model Training
- Model Prediction
- Accuracy Score
- Classification Report
- Confusion Matrix

## Implementation

- Loaded the Breast Cancer dataset using Scikit-learn.
- Split the dataset into training and testing sets (80:20).
- Applied StandardScaler for feature scaling.
- Trained a Logistic Regression model.
- Predicted cancer classifications on test data.
- Evaluated model performance using accuracy, classification report, and confusion matrix.

## Model Evaluation

The model is evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- Confusion Matrix

## Goal

To understand how Logistic Regression works for binary classification and learn how to train and evaluate a classification model using Scikit-learn.

## Note

This is an educational machine learning project. Its predictions should not be used for actual medical diagnosis or treatment decisions.