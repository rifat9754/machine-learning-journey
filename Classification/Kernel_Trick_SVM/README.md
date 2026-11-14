# Kernel Trick in Support Vector Machine (SVM) – Non-Linear Classification

## Overview

This project demonstrates the **Kernel Trick in Support Vector Machine (SVM)** for solving non-linear classification problems using Python and Scikit-learn.

A Radial Basis Function (RBF) kernel is used to classify data points that cannot be effectively separated using a straight-line decision boundary.

The project generates a circular synthetic dataset, trains an SVM classifier, evaluates its performance, and visualizes the non-linear decision boundary.

## Algorithm Used

### Support Vector Machine (SVM)

Support Vector Machine is a supervised machine learning algorithm used for classification and regression.

It finds an optimal decision boundary (hyperplane) that separates different classes.

### Kernel Trick

The Kernel Trick allows SVM to handle non-linear classification problems by implicitly mapping data into a higher-dimensional feature space.

Instead of explicitly transforming the data into higher dimensions, a kernel function calculates the required similarity between data points.

### RBF Kernel (Radial Basis Function)

This project uses the RBF kernel:

```python
SVC(kernel="rbf")
```

The RBF kernel is useful when the relationship between input features and target classes is non-linear.

Its mathematical representation is:

\[
K(x_i,x_j)=\exp(-\gamma\|x_i-x_j\|^2)
\]

Where:

- \(x_i, x_j\) are data points.
- \(\gamma\) controls how far the influence of a training point reaches.
- \(K\) represents the similarity between two data points.

## Dataset

The project uses a synthetic circular dataset generated with Scikit-learn's `make_circles()` function.

```python
from sklearn.datasets import make_circles

X, y = make_circles(
    100,
    factor=0.1,
    noise=0.1
)
```

Dataset characteristics:

| Property | Value |
|---|---|
| Dataset | Synthetic Circular Dataset |
| Total Samples | 100 |
| Number of Classes | 2 |
| Features | 2 |
| Factor | 0.1 |
| Noise | 0.1 |

The dataset contains two circular classes, making it suitable for demonstrating non-linear classification.

## Implementation Workflow

1. Import the required Python libraries.
2. Generate a circular dataset using `make_circles()`.
3. Visualize the dataset using Matplotlib.
4. Split the dataset into training and testing sets using `train_test_split()`.
5. Use 80% of the data for training and 20% for testing.
6. Create an SVM classifier using the RBF kernel.
7. Train the classifier using `fit()`.
8. Generate predictions using `predict()`.
9. Evaluate the model using accuracy and classification metrics.
10. Visualize the non-linear decision boundary.

## Model Configuration

```python
from sklearn.svm import SVC

rbf_classifier = SVC(kernel="rbf")

rbf_classifier.fit(X_train, y_train)
```

| Parameter | Description |
|---|---|
| `kernel="rbf"` | Uses the Radial Basis Function kernel |
| `test_size=0.20` | Uses 20% of the dataset for testing |
| `factor=0.1` | Controls the relative size of the inner circle |
| `noise=0.1` | Adds noise to the generated dataset |

The notebook uses the default values of other SVC parameters, including `C` and `gamma`.

## Model Evaluation

The model generates predictions on the test dataset and evaluates them using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- Classification Report

The notebook also imports `confusion_matrix`, although it does not currently display the confusion matrix.

## Visualization

The project includes:

- Circular dataset visualization.
- Two-class data distribution.
- Non-linear SVM decision boundary.
- Colored decision regions showing the predicted classes.

The decision boundary is visualized using Matplotlib's `contourf()` function.

## Technologies & Libraries

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

## Project Structure

```text
Kernel-Trick-SVM/
│
├── Kernel-trick-SVM.ipynb
└── README.md
```

## Learning Outcomes

After completing this project, you will understand:

- The basic concept of the Kernel Trick.
- Why linear SVM is not always suitable for non-linear datasets.
- How the RBF kernel handles non-linear classification.
- How to generate circular datasets using `make_circles()`.
- How to train an SVM model using Scikit-learn.
- How to evaluate a classification model.
- How to visualize non-linear decision boundaries.

## Future Improvements

- Experiment with different kernel functions such as Linear and Polynomial.
- Tune the `C` and `gamma` hyperparameters.
- Apply feature scaling using StandardScaler.
- Visualize the confusion matrix.
- Compare the performance of Linear SVM and RBF SVM.

---

**Part of my Machine Learning Journey** – Learning and implementing machine learning algorithms using Python and Scikit-learn.