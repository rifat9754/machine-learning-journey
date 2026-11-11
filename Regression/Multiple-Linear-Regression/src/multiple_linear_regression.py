
import numpy as np


class MultipleLinearRegression:

    def __init__(self, learning_rate=0.01, epochs=5000):
        self.learning_rate = learning_rate
        self.epochs = epochs

        self.weights = None
        self.bias = 0.0

        self.mean = None
        self.std = None

        self.loss_history = []

    def fit(self, X, y):

        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float).reshape(-1)

        if X.ndim != 2:
            raise ValueError("X must be a 2D array.")

        if len(X) != len(y):
            raise ValueError("X and y must have equal sample counts.")

        if not np.all(np.isfinite(X)) or not np.all(np.isfinite(y)):
            raise ValueError("X and y must contain finite values.")

        # Feature scaling
        self.mean = X.mean(axis=0)
        self.std = X.std(axis=0)

        self.std[self.std == 0] = 1.0

        X_scaled = (X - self.mean) / self.std

        n_samples, n_features = X_scaled.shape

        # Initialize parameters
        self.weights = np.zeros(n_features)
        self.bias = 0.0

        self.loss_history = []

        # Gradient Descent
        for epoch in range(self.epochs):

            y_pred = np.dot(X_scaled, self.weights) + self.bias

            errors = y_pred - y

            dw = (2 / n_samples) * np.dot(X_scaled.T, errors)
            db = (2 / n_samples) * np.sum(errors)

            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

            loss = np.mean(errors ** 2)
            self.loss_history.append(loss)

        return self

    def predict(self, X):

        if self.weights is None:
            raise ValueError("Train the model before prediction.")

        X = np.asarray(X, dtype=float)

        if X.ndim == 1:
            X = X.reshape(1, -1)

        if X.ndim != 2 or X.shape[1] != len(self.weights):
            raise ValueError("Input features do not match training features.")

        X_scaled = (X - self.mean) / self.std

        return np.dot(X_scaled, self.weights) + self.bias

    def score(self, X, y):

        y = np.asarray(y, dtype=float).reshape(-1)
        y_pred = self.predict(X)

        ss_total = np.sum((y - np.mean(y)) ** 2)
        ss_residual = np.sum((y - y_pred) ** 2)

        if ss_total == 0:
            raise ValueError("R2 score is undefined for constant targets.")

        return 1 - (ss_residual / ss_total)
