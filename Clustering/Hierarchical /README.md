# Hierarchical Clustering – Agglomerative Clustering with Dendrogram

## Overview

This project demonstrates **Hierarchical Clustering**, an unsupervised machine learning algorithm, using Python and Scikit-learn.

The project generates a synthetic dataset using `make_blobs`, visualizes the hierarchical relationships between data points through a Dendrogram, and applies Agglomerative Clustering to group the data into three clusters.

## Algorithm Used

**Agglomerative Hierarchical Clustering**

Agglomerative Clustering is a bottom-up hierarchical clustering approach. Initially, each data point is treated as an individual cluster. The algorithm repeatedly merges the closest clusters until the desired number of clusters is reached.

## Technologies & Libraries

- Python
- Matplotlib
- SciPy
- Scikit-learn

## Dataset

The project uses a synthetic dataset generated with Scikit-learn's `make_blobs()` function.

Dataset configuration:

- Number of samples: 50
- Number of centers: 3
- Cluster standard deviation: 0.6
- Random state: 42

## Project Workflow

1. **Import Libraries** – Import Matplotlib, SciPy and Scikit-learn modules.
2. **Generate Dataset** – Create 50 synthetic data points using `make_blobs()`.
3. **Dendrogram Visualization** – Generate a Dendrogram using SciPy's `linkage()` function with Ward's method.
4. **Model Training** – Train an Agglomerative Clustering model with 3 clusters.
5. **Cluster Prediction** – Assign each data point to a cluster using `fit_predict()`.
6. **Result Visualization** – Visualize the three resulting clusters using a scatter plot.

## Model Configuration

```python
hc = AgglomerativeClustering(
    n_clusters=3,
    metric='euclidean',
    linkage='ward'
)

y_hc = hc.fit_predict(X)
```

| Parameter | Value |
|---|---|
| Algorithm | Agglomerative Clustering |
| Number of Clusters | 3 |
| Distance Metric | Euclidean |
| Linkage Method | Ward |

## Dendrogram

A Dendrogram is a tree-like diagram that illustrates how individual data points or clusters are merged during hierarchical clustering.

This project uses:

```python
sch.dendrogram(
    sch.linkage(X, method='ward')
)
```

Ward's linkage method merges clusters based on the increase in within-cluster variance.

## Result Visualization

The final scatter plot displays the three clusters using different colors:

- Red – Cluster 1
- Blue – Cluster 2
- Green – Cluster 3

## Project Structure

```text
Hierarchical-Clustering/
│
├── Hierarchical_clustering.ipynb
└── README.md
```

## Key Learnings

- Understanding Hierarchical Clustering.
- Learning the Agglomerative Clustering approach.
- Understanding Dendrogram visualization.
- Exploring Ward's linkage method.
- Applying Euclidean distance for clustering.
- Visualizing unsupervised learning results.

## Conclusion

This project demonstrates how Agglomerative Hierarchical Clustering groups data points into clusters and how a Dendrogram helps visualize the hierarchical merging process.

It provides practical experience with hierarchical clustering using SciPy and Scikit-learn.