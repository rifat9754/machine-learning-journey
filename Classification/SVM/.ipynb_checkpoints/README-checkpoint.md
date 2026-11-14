# Support Vector Machine (SVM) – Classification

## Overview

This project demonstrates **Support Vector Machine (SVM)**, a supervised machine learning algorithm used for classification.

The implementation uses Python and Scikit-learn to explore how SVM separates different classes using a linear decision boundary.

The notebook covers:
- Generating a synthetic dataset using `make_blobs()`
- Training a Linear Support Vector Classifier
- Visualizing the decision boundary and margins
- Identifying support vectors
- Comparing different values of the regularization parameter `C`

## Algorithm Used

### Support Vector Machine (SVM)

Support Vector Machine is a supervised learning algorithm that finds an optimal decision boundary (hyperplane) to separate different classes.

Its primary objective is to maximize the margin between the decision boundary and the closest data points from each class.

### Key Concepts

**1. Hyperplane**

A hyperplane is the decision boundary that separates different classes.

**2. Margin**

The margin is the distance between the decision boundary and the closest data points from each class.

**3. Support Vectors**

Support vectors are the data points closest to the decision boundary. They play an important role in determining the optimal hyperplane.

**4. Regularization Parameter (C)**

The `C` parameter controls the trade-off between maximizing the margin and minimizing classification errors.

- High C: Penalizes classification errors more heavily.
- Low C: Allows more margin violations and generally favors a wider margin.

## Dataset

This project uses a synthetic dataset generated with Scikit-learn's `make_blobs()` function.

Two datasets are used:

| Dataset | Samples | Classes | Cluster Standard Deviation |
|---|---:|---:|---:|
| Linear Dataset | 50 | 2 | 0.60 |
| Almost Linearly Separable Dataset | 100 | 2 | 0.80 |

The datasets contain two input features and two target classes.

## Implementation Workflow

1. Import the required Python libraries.
2. Generate a synthetic linear dataset using `make_blobs()`.
3. Visualize the dataset using Matplotlib.
4. Create an SVM classifier using `SVC(kernel='linear', C=1)`.
5. Train the model using `model.fit(X, y)`.
6. Create a visualization function for the decision boundary and margins.
7. Identify and visualize support vectors.
8. Generate an almost linearly separable dataset.
9. Compare the effects of different C values (`100.0` and `0.01`).

## Technologies & Libraries

- Python
- NumPy
- Matplotlib
- SciPy
- Seaborn
- Scikit-learn

## Important Parameters

| Parameter | Description |
|---|---|
| `kernel='linear'` | Uses a linear decision boundary |
| `C=1` | Regularization parameter for the initial model |
| `C=100.0` | Higher penalty for classification errors |
| `C=0.01` | Lower penalty for classification errors |
| `n_samples=50` | Number of samples in the first dataset |
| `n_samples=100` | Number of samples in the second dataset |

## Visualizations

The notebook includes visualizations of:

- Two-class synthetic datasets
- Linear SVM decision boundary
- Positive and negative margin boundaries
- Support vectors highlighted with hollow circles
- Comparison of SVM decision boundaries using different C values

## Project Structure

```text
Support-Vector-Machine/
│
├── SVM.ipynb
└── README.md
```

## Learning Outcomes

After completing this project, you will understand:

- The basic working principle of Support Vector Machine.
- How a linear SVM classifier separates two classes.
- The meaning of hyperplanes and margins.
- The role of support vectors in determining the decision boundary.
- How the regularization parameter C affects the SVM model.
- How to visualize SVM decision boundaries using Matplotlib and Scikit-learn.

## Future Improvements

- Apply feature scaling using StandardScaler.
- Split the dataset into training and testing sets.
- Evaluate the classifier using accuracy, precision, recall, and F1-score.
- Experiment with Polynomial and RBF kernels.
- Apply SVM to a real-world classification dataset.

---

**Part of my Machine Learning Journey** – Learning and implementing machine learning algorithms using Python and Scikit-learn.