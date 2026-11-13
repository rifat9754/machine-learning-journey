# K-Means Clustering – Iris Dataset

## Overview

This project implements **K-Means Clustering**, an unsupervised machine learning algorithm, using the Iris dataset from Scikit-learn.

K-Means groups similar data points into a predefined number of clusters based on their feature values. In this project, the first two features of the Iris dataset are used to create three clusters and visualize their centroids.

## Dataset

- **Dataset:** Iris Dataset
- **Source:** Scikit-learn
- **Total Samples:** 150
- **Features Used:**
  - Sepal Length (cm)
  - Sepal Width (cm)
- **Number of Clusters:** 3

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## Project Workflow

1. Import required libraries.
2. Load the Iris dataset.
3. Select the first two features (Sepal Length and Sepal Width).
4. Convert the selected features into a Pandas DataFrame.
5. Visualize the distribution of Sepal Length.
6. Initialize the K-Means clustering model.
7. Train the model using the selected features.
8. Predict cluster labels for the data points.
9. Extract cluster centroids.
10. Visualize the clusters and their centroids.

## Model Configuration

The K-Means model is initialized with three clusters.

```python
kmeans = KMeans(
    n_clusters=3,
    random_state=42
)

kmeans.fit(X)
```

## Predictions

The trained model predicts the cluster assigned to each data point and extracts the cluster centroids.

```python
y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_
```

## Visualizations

- Sepal Length Distribution Plot
- K-Means Clustering Scatter Plot
- Cluster Centroids

The scatter plot displays data points using different colors for each cluster. Red X markers represent the cluster centroids.

## Key Concepts Learned

- Unsupervised Learning
- Clustering
- K-Means Algorithm
- Cluster Centroids
- Feature Selection
- Data Visualization
- Scikit-learn Model Training and Prediction

## How to Run

1. Clone the repository.
2. Install the required libraries:

```bash
pip install pandas matplotlib seaborn scikit-learn jupyter
```

3. Start Jupyter Notebook:

```bash
jupyter notebook
```

4. Open `K-mean.ipynb`.
5. Run all cells.

## Author

**Ahanaf Tahmid Rifat**

GitHub: [rifat9754](https://github.com/rifat9754)

---

*Part of my Machine Learning Journey – implementing machine learning algorithms using Python and Scikit-learn.*