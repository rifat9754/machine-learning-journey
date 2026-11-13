# Random Forest Classification – Breast Cancer Classification

## Overview

This project implements the **Random Forest Classification** algorithm to classify breast cancer tumors using the Breast Cancer Wisconsin dataset provided by Scikit-learn.

Random Forest is a supervised Machine Learning algorithm that combines multiple Decision Trees to make predictions. For classification, the final prediction is determined through majority voting among the trees.

## Dataset

- **Dataset:** Breast Cancer Wisconsin Dataset
- **Source:** Scikit-learn built-in dataset
- **Total Samples:** 569
- **Input Features:** 30
- **Target Classes:** 2

### Target Classes

- Malignant
- Benign

### Input Features

The dataset contains 30 numerical features describing characteristics of cell nuclei, including:

- Mean Radius
- Mean Texture
- Mean Perimeter
- Mean Area
- Mean Smoothness
- Mean Compactness
- Mean Concavity
- Mean Symmetry

Other features include standard error and worst-value measurements.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

## Algorithm

**Random Forest Classifier**

The project uses `RandomForestClassifier` with the following configuration:

- **Number of Trees (`n_estimators`):** 100
- **Maximum Depth (`max_depth`):** 5
- **Random State:** 42

## Implementation Steps

1. Import the required libraries.
2. Load the Breast Cancer Wisconsin dataset.
3. Separate input features and target labels.
4. Convert input features into a Pandas DataFrame.
5. Visualize the distribution of Mean Radius.
6. Analyze feature correlations using a heatmap.
7. Split the dataset into training and testing sets (80:20).
8. Train the Random Forest Classifier.
9. Generate predictions on test data.
10. Compare actual and predicted values.
11. Evaluate model accuracy.
12. Generate a classification report.
13. Identify and visualize the top 10 important features.

## Model Evaluation

The project uses the following evaluation methods:

- **Accuracy Score:** Measures the percentage of correctly classified samples.
- **Classification Report:** Provides precision, recall, F1-score, and support for each class.

## Feature Importance

Random Forest provides feature importance scores that help identify which input features contribute most to the model's predictions.

The project visualizes the **Top 10 Important Features** using a Seaborn bar plot.

## Data Visualization

The notebook includes:

- Mean Radius Distribution Plot
- Feature Correlation Heatmap
- Top 10 Feature Importance Plot

## Key Concepts Learned

- Supervised Learning
- Classification
- Ensemble Learning
- Random Forest Algorithm
- Decision Trees
- Bootstrap Aggregation (Bagging)
- Training and Testing Data Split
- Model Training and Prediction
- Accuracy Score
- Classification Report
- Precision, Recall, and F1-score
- Feature Importance

## Project Goal

The goal of this project is to understand how the Random Forest algorithm combines multiple Decision Trees and implement a binary classification model using Scikit-learn.

## Note

This is an educational Machine Learning project developed to practice Random Forest Classification. It is not intended for medical diagnosis or clinical decision-making.