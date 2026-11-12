# KNN Regression – California Housing Price Prediction

## Overview

This project implements the **K-Nearest Neighbors (KNN) Regression** algorithm to predict house prices using the California Housing dataset from Scikit-learn.

KNN Regression is a supervised Machine Learning algorithm that predicts a numerical value by calculating the average target values of its nearest neighbors.

## Dataset

- **Dataset:** California Housing Dataset
- **Source:** Scikit-learn
- **Total Samples:** 20,640
- **Input Features:** 8
- **Target Variable:** Median House Value

### Input Features

- MedInc – Median Income
- HouseAge – Median House Age
- AveRooms – Average Rooms
- AveBedrms – Average Bedrooms
- Population – Population
- AveOccup – Average Occupancy
- Latitude – Latitude
- Longitude – Longitude

### Target

- Price – Median House Value (in units of $100,000)

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

## Algorithm

**K-Nearest Neighbors (KNN) Regressor**

The project uses `KNeighborsRegressor` with:

- Number of neighbors (`K`): 5
- Distance-based neighbor selection
- Average of neighboring target values for prediction
- Feature scaling using `StandardScaler`

## Implementation Steps

1. Import required libraries.
2. Load the California Housing dataset.
3. Convert the dataset into a Pandas DataFrame.
4. Explore dataset information and statistical summaries.
5. Check missing values.
6. Visualize house price distribution.
7. Analyze feature correlations using a heatmap.
8. Split data into training and testing sets (80:20).
9. Apply feature scaling using StandardScaler.
10. Train the KNN Regression model.
11. Generate predictions on test data.
12. Compare actual and predicted values.
13. Evaluate model performance.
14. Visualize actual versus predicted values.
15. Analyze prediction errors using a residual plot.
16. Perform custom house price prediction.

## Model Evaluation

The model performance is evaluated using:

- **MAE (Mean Absolute Error):** Measures the average absolute prediction error.
- **MSE (Mean Squared Error):** Measures the average squared prediction error.
- **RMSE (Root Mean Squared Error):** Measures the square root of MSE.
- **R² Score:** Measures how well the model explains the variance in the target variable.

## Data Visualization

The project includes:

- House Price Distribution Plot
- Correlation Heatmap
- Actual vs Predicted Plot
- Residual Plot

## Key Concepts Learned

- Supervised Learning
- Regression
- K-Nearest Neighbors Algorithm
- Distance-Based Prediction
- Training and Testing Data Split
- Feature Scaling
- StandardScaler
- Model Training and Prediction
- MAE, MSE, RMSE and R²
- Residual Analysis
- Custom Prediction

## Custom Prediction

The trained model can predict the median house value for a custom input containing eight housing features.

The prediction is converted from the dataset's $100,000 unit into USD for easier interpretation.

## Project Goal

The goal of this project is to understand how the KNN Regression algorithm works and implement a house price prediction model using Scikit-learn.

## Note

This is an educational Machine Learning project developed to practice the KNN Regression algorithm. The dataset represents historical California housing data and should not be treated as a source of current property valuations.