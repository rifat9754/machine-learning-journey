class LinearRegressionScratch:

    def __init__(self, learning_rate=0.05, epochs=3000):
        self.learning_rate = learning_rate
        self.epochs = epochs

        self.w = 0.0
        self.b = 0.0

        self.loss_history = []

    def fit(self, X, y):

        X = np.asarray(X).reshape(-1)
        y = np.asarray(y)

        n = len(X)

        for epoch in range(self.epochs):

            y_pred = self.w * X + self.b

            errors = y_pred - y

            dw = (2 / n) * np.sum(errors * X)
            db = (2 / n) * np.sum(errors)

            self.w -= self.learning_rate * dw
            self.b -= self.learning_rate * db

            loss = np.mean(errors ** 2)
            self.loss_history.append(loss)

        return self

    def predict(self, X):

        X = np.asarray(X).reshape(-1)

        return self.w * X + self.b

    def mean_squared_error(self, y_true, y_pred):

        return np.mean((y_true - y_pred) ** 2)

    def score(self, y_true, y_pred):

        ss_total = np.sum((y_true - np.mean(y_true)) ** 2)
        ss_residual = np.sum((y_true - y_pred) ** 2)

        return 1 - (ss_residual / ss_total)


# Train Our Custom Class

scratch_model = LinearRegressionScratch(
    learning_rate=0.05,
    epochs=3000
)

scratch_model.fit(X_train_scaled, y_train)

print("Weight:", scratch_model.w)
print("Bias:", scratch_model.b)

# Make Predictions

scratch_predictions = scratch_model.predict(X_test_scaled)

print("Actual:", y_test[:5])
print("Predicted:", scratch_predictions[:5])

#Evaluate Our Custom Class

scratch_mse = scratch_model.mean_squared_error(
    y_test,
    scratch_predictions
)

scratch_r2 = scratch_model.score(
    y_test,
    scratch_predictions
)

print("MSE:", scratch_mse)
print("R2 Score:", scratch_r2)