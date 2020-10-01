import numpy as np
class Perceptron(object):
    """
    Perceptron classifier
    ___________________
    parameters
    __________________
    eta: float
    learning rate betweeen 0.0 and 1.0
    n_iter: int
    Passes over the training dataset

    ___________________
    Attributes
    ___________________
    w_: 1d array
    weights after training
    errors_: list
    Number of msiclassifications for every epoch
    """
    def __init__(self, eta, n_iter):
        self.eta = eta
        self.n_iter = n_iter
    
    def fit(self, X, y):
        """
        Fit training data
        ______________________
        parameters
        ______________________
        X: {array-like}, shape = [n_samples, n_features]
            Training vectors where n_samples is the number of samples
            and n_features is the number of features
        y: array-like, shape = [n_samples]
            Target values

        ____________________
        Returns
        ____________________
        self: object
        """
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi,target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self
    
    def net_input(self, X):
        """
        Calculate net input
        """
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        """
        Return class label after unit step
        """
        return np.where(self.net_input(X) >= 0.0, 1, -1)