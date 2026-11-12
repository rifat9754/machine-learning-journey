# K-Nearest Neighbors (KNN) – Iris Flower Classification

## Overview

This project implements the **K-Nearest Neighbors (KNN)** algorithm to classify Iris flowers into their respective species using the Iris dataset from Scikit-learn.

KNN is a supervised Machine Learning algorithm that classifies a data point based on the majority class among its nearest neighbors.

## Dataset

- **Dataset:** Iris Dataset
- **Source:** Scikit-learn built-in dataset
- **Total Samples:** 150
- **Input Features:** 4
- **Target Classes:** 3

### Input Features

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

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

**K-Nearest Neighbors (KNN) Classifier**

The project uses `KNeighborsClassifier` with:

- Number of neighbors (`K`): 3
- Distance-based nearest neighbor classification
- Feature scaling using `StandardScaler`

## Implementation Steps

1. Import required libraries.
2. Load the Iris dataset.
3. Convert the dataset into a Pandas DataFrame.
4. Separate input features and target labels.
5. Split the dataset into training and testing sets (80:20).
6. Apply feature scaling using StandardScaler.
7. Train the KNN classifier with K = 3.
8. Predict flower species using the test dataset.
9. Evaluate model accuracy.
10. Visualize the confusion matrix using Seaborn.

## Model Evaluation

The model uses the following evaluation method:

- Accuracy Score
- Confusion Matrix

## Key Concepts Learned

- Supervised Learning
- Classification
- K-Nearest Neighbors algorithm
- Training and Testing Data Split
- Feature Scaling
- StandardScaler
- Model Training and Prediction
- Accuracy Score
- Confusion Matrix

## Project Goal

The goal of this project is to understand how the K-Nearest Neighbors algorithm works and implement a basic classification model using Scikit-learn.

## Note

This is an educational Machine Learning project developed to practice the KNN classification algorithm.