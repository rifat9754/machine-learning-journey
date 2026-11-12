# Decision Tree Classification – Iris Flower Classification

## Overview

This project implements the **Decision Tree Classification** algorithm to classify Iris flowers into three different species using the Iris dataset from Scikit-learn.

A Decision Tree is a supervised Machine Learning algorithm that makes predictions by learning decision rules from the input features.

## Dataset

- **Dataset:** Iris Dataset
- **Source:** Scikit-learn built-in dataset
- **Total Samples:** 150
- **Input Features:** 4
- **Target Classes:** 3

### Input Features

- Sepal Length (cm)
- Sepal Width (cm)
- Petal Length (cm)
- Petal Width (cm)

### Target Classes

- Setosa
- Versicolor
- Virginica

## Technologies Used

- Python
- Pandas
- Seaborn
- Matplotlib
- Scikit-learn

## Algorithm

**Decision Tree Classifier**

The project uses `DecisionTreeClassifier` with the following configuration:

- **Criterion:** Gini
- **Maximum Depth:** 4
- **Random State:** 42

## Implementation Steps

1. Import the required libraries.
2. Load the Iris dataset.
3. Separate input features and target labels.
4. Convert the dataset into a Pandas DataFrame.
5. Visualize sepal length distribution.
6. Analyze feature correlations using a heatmap.
7. Split the dataset into training and testing sets (80:20).
8. Apply feature scaling using StandardScaler.
9. Train the Decision Tree Classifier.
10. Predict Iris flower species.
11. Compare actual and predicted values.
12. Evaluate model accuracy.
13. Visualize the confusion matrix.
14. Visualize the trained Decision Tree structure.

## Model Evaluation

The project uses:

- **Accuracy Score:** Measures the percentage of correctly classified samples.
- **Confusion Matrix:** Shows correct and incorrect predictions for each class.

## Data Visualization

The notebook includes:

- Sepal Length Distribution Plot
- Feature Correlation Heatmap
- Confusion Matrix Heatmap
- Decision Tree Visualization

## Key Concepts Learned

- Supervised Learning
- Classification
- Decision Tree Algorithm
- Gini Impurity
- Training and Testing Data Split
- Feature Scaling
- Model Training and Prediction
- Accuracy Score
- Confusion Matrix
- Decision Tree Visualization
- Maximum Tree Depth

## Project Goal

The goal of this project is to understand how the Decision Tree Classification algorithm works and implement a multi-class classification model using Scikit-learn.

## Note

This is an educational Machine Learning project developed to practice Decision Tree Classification using the Iris dataset.