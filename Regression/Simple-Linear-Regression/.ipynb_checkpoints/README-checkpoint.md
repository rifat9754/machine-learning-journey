# Simple Linear Regression – Student Marks Prediction

A Machine Learning project that predicts students' marks based on the number of hours they study using **Simple Linear Regression**.

This project implements Linear Regression from scratch using NumPy and compares the results with Scikit-learn's implementation.

## Project Overview

The goal of this project is to understand how Simple Linear Regression works and how it can be implemented without relying entirely on Machine Learning libraries.

A synthetic dataset containing students' study hours and marks is used to train and evaluate the models.

## Objectives

- Understand the fundamentals of Simple Linear Regression.
- Perform Exploratory Data Analysis (EDA).
- Implement Linear Regression from scratch using NumPy.
- Understand and implement Gradient Descent.
- Train a Linear Regression model using Scikit-learn.
- Evaluate and compare model performance.
- Visualize the regression line and predictions.
- Save and load a trained model.

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Joblib

## Project Structure

```text
Simple-Linear-Regression/
│
├── README.md
├── requirements.txt
├── Simple_Linear_Regression.ipynb
│
├── data/
│   └── student_scores.csv
│
├── images/
│
├── models/
│   └── linear_regression_model.pkl
│
└── src/
    └── linear_regression_from_scratch.py
```

## Dataset

The project uses a synthetic dataset generated with NumPy.

| Feature | Description |
|---|---|
| Hours | Number of hours a student studies |
| Marks | Marks obtained by the student |

The dataset contains 200 samples.

**Note:** This is a synthetically generated dataset, not real-world student data.

## Mathematical Concept

Simple Linear Regression models the relationship between one independent variable and one dependent variable.

The equation is:

\[
\hat{y} = wx + b
\]

Where:

- \(x\) = Study hours
- \(\hat{y}\) = Predicted marks
- \(w\) = Weight (slope)
- \(b\) = Bias (intercept)

### Gradient Descent

Gradient Descent is used to optimize the model parameters by minimizing the Mean Squared Error (MSE).

\[
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
\]

## Project Workflow

1. Dataset generation and loading
2. Exploratory Data Analysis
3. Data cleaning and preprocessing
4. Feature and target selection
5. Train-test splitting
6. Feature scaling
7. Linear Regression implementation using NumPy
8. Gradient Descent optimization
9. Model training using Scikit-learn
10. Model evaluation and comparison
11. Data visualization
12. Making predictions for new inputs
13. Saving and loading the trained model

## Model Evaluation

The models are evaluated using the following metrics:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

Both the NumPy implementation and Scikit-learn model are compared using the same test dataset.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/machine-learning-journey.git
```

### 2. Navigate to the project directory

```bash
cd machine-learning-journey/Regression/Simple-Linear-Regression
```

### 3. Create a virtual environment (optional)

```bash
python -m venv venv
```

Activate it:

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Jupyter Notebook

```bash
jupyter notebook
```

Open `Simple_Linear_Regression.ipynb` and execute the cells sequentially.

## Results

The project compares two implementations:

1. Linear Regression from scratch using NumPy.
2. Linear Regression using Scikit-learn.

The evaluation metrics and visualizations help understand how well each model predicts student marks.

## Learning Outcomes

Through this project, I learned:

- How Simple Linear Regression works mathematically.
- How to implement Gradient Descent.
- How model parameters are optimized.
- How to perform EDA and feature scaling.
- How to evaluate Machine Learning models.
- How to use Scikit-learn for model training and prediction.

## Author

**Machine Learning Journey**

This project is part of my journey to become an AI/ML Engineer.

More Machine Learning algorithms and projects will be added to this repository as I continue learning.