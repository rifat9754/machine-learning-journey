# AdaBoost Classification – Breast Cancer Classification

## Overview

This project implements **AdaBoost (Adaptive Boosting)** for binary classification using the Breast Cancer Wisconsin dataset from Scikit-learn.

AdaBoost is an ensemble learning algorithm that combines multiple weak learners to build a stronger classifier. In this project, a Decision Tree with `max_depth=1` is used as the base estimator.

## Dataset

- **Dataset:** Breast Cancer Wisconsin Dataset
- **Source:** Scikit-learn
- **Total Samples:** 569
- **Total Features:** 30
- **Target Classes:** 
  - Malignant
  - Benign

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## Project Workflow

1. Import required libraries.
2. Load the Breast Cancer dataset.
3. Convert features into a Pandas DataFrame.
4. Explore the dataset.
5. Visualize feature distribution.
6. Generate a correlation heatmap.
7. Split the dataset into training and testing sets.
8. Create a Decision Tree base estimator.
9. Train the AdaBoost classifier.
10. Predict test-set classes.
11. Evaluate model performance.

## Model Configuration

**Base Estimator:** DecisionTreeClassifier

```python
base_estimator = DecisionTreeClassifier(max_depth=1)
```

**AdaBoost Classifier:**

```python
adaboost = AdaBoostClassifier(
    estimator=base_estimator,
    learning_rate=1.0,
    random_state=42
)

adaboost.fit(X_train, y_train)
```

## Train-Test Split

- Training Set: 80%
- Testing Set: 20%
- Random State: 42

## Model Evaluation

The model is evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- Classification Report

## Visualizations

- Mean Radius Distribution
- Feature Correlation Heatmap

## Key Concepts Learned

- Ensemble Learning
- Boosting
- AdaBoost Algorithm
- Weak Learners
- Decision Tree as a Base Estimator
- Train-Test Split
- Classification Metrics
- Data Visualization

## How to Run

1. Clone the repository.
2. Install the required libraries:

```bash
pip install pandas matplotlib seaborn scikit-learn jupyter
```

3. Open Jupyter Notebook:

```bash
jupyter notebook
```

4. Open `Adaboost_Algorithm.ipynb`.
5. Run all cells.

## Author

**Ahanaf Tahmid Rifat**

GitHub: [rifat9754](https://github.com/rifat9754)

---

*Part of my Machine Learning Journey – learning and implementing machine learning algorithms using Python and Scikit-learn.*