import util
import numpy as np

class KNN():
    """ K Nearest Neighbors Classifier 

    Attributes:

        k (int): How many neighbors to consider (default: 5)
        dist_func (Callable): Distance function (default: euclidean_distance)
        X (np.array): Input training data
        Y (np.array): Output (e.g., gold prediction) training data
    """
    def __init__(self, task, k:int=5, dist_func=util.euclidean_distance):
        self.task = task
        self.k = k
        self.dist_func = dist_func

    def fit(self, X, Y):
        """ Adds X and Y from train to class """ 
        self.X = X
        self.Y = Y

    def predict(self, X_test: np.array) -> np.array:
        """ Makes prediction based on k closest neighbors and classification task

        Args:
            X_test (np.array): Input test data

        Returns:
            np.array: Predictions; labels if self.task is classification or values if self.task is regression
        """ 
        pass

if __name__ == '__main__':

    x = np.array([[1,2,3], [2,0,1], [4,4,2], [3,2,0], [1,5,1]]) 
    y_labels = np.array(['A', 'C', 'B', 'A', 'B'])
    y_values = np.array([3, 5, -1, 2, 0])

    ## Write test cases using the toy data above (or you can create your own toy data!)
    