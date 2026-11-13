# DBSCAN Clustering – Moon-Shaped Dataset

## Overview

This project demonstrates **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**, an unsupervised machine learning algorithm used to identify clusters based on the density of data points.

The project uses a synthetic moon-shaped dataset generated with Scikit-learn's `make_moons()` function and applies DBSCAN to identify clusters.

## Algorithm Used

**DBSCAN (Density-Based Spatial Clustering)**

DBSCAN groups together data points that are closely packed and identifies points in low-density regions as noise or outliers.

Unlike K-Means, DBSCAN does not require the number of clusters to be specified beforehand.

## Technologies & Libraries

- Python
- Matplotlib
- Scikit-learn

## Dataset

The project uses a synthetic moon-shaped dataset generated using `make_moons()`.

Dataset configuration:

- Number of samples: 250
- Noise: 0.05
- Random state: 42

```python
X, _ = make_moons(
    n_samples=250,
    noise=0.05,
    random_state=42
)
```

## Project Workflow

1. **Import Libraries** – Import Matplotlib, DBSCAN and `make_moons`.
2. **Generate Dataset** – Create 250 moon-shaped data points.
3. **Model Initialization** – Initialize the DBSCAN model.
4. **Cluster Prediction** – Apply `fit_predict()` to assign cluster labels.
5. **Result Visualization** – Visualize the clustering results using a scatter plot.

## Model Configuration

```python
dbscan = DBSCAN(
    eps=0.2,
    min_samples=5
)

y_pred = dbscan.fit_predict(X)
```

| Parameter | Value |
|---|---|
| Algorithm | DBSCAN |
| eps | 0.2 |
| min_samples | 5 |

### Important Parameters

- **eps:** Maximum distance between two samples for them to be considered neighbors.
- **min_samples:** Minimum number of samples required to form a dense region.

DBSCAN uses the label `-1` to identify noise points.

## Result Visualization

The project visualizes the clustering results using Matplotlib's scatter plot.

```python
plt.figure(figsize=(8, 5))

plt.scatter(
    X[:, 0],
    X[:, 1],
    c=y_pred,
    cmap='plasma',
    s=40
)

plt.title("DBSCAN Clustering on Moon-shaped Data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
```

Different colors represent the cluster labels assigned by DBSCAN. Noise points, if detected, are represented by the label `-1`.

## Key Learnings

- Understanding density-based clustering.
- Learning how DBSCAN identifies dense regions.
- Understanding `eps` and `min_samples`.
- Identifying noise and outliers.
- Applying DBSCAN to non-linear moon-shaped data.
- Visualizing unsupervised learning results.

## Conclusion

This project demonstrates how DBSCAN can identify clusters in non-linear, moon-shaped datasets based on data-point density.

It provides practical experience with density-based clustering using Scikit-learn.