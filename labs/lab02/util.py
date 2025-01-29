import doctest
import numpy as np


def mse(pred:np.array, true:np.array) -> float:
    """
    Input:
        pred: numpy array of predicted values
        true: numpy array of true values
    Output: 
        Mean squared error as float; rounded to two decimal points

    >>> mse(np.array([3,2,1]), np.array([3,1,2]))
    0.67
    
    >>> mse(np.array([10, 15, -4, 0]), np.array([0, 15, 4, 0]))
    41.0

    """
    pass


def accuracy(pred:np.array, true:np.array) -> float:
    """
    Input:
        pred: numpy array of predicted labels
        true: numpy array of true labels
    Output:
        accuracy: float as percent; rounded to two decimal points

    >>> accuracy(np.array([1,1,1,1,1,0]), np.array([0,0,1,1,1,1]))
    50.0

    >>> accuracy(np.array(['A','A','B','A', 'A', 'C', 'C']), np.array(['C','A','B','A', 'A', 'C', 'B']))
    71.43
    """
    pass

def precision(pred:np.array, true:np.array) -> float:
    """
    Input:
        pred: numpy array of predicted labels
        true: numpy array of true labels
    Output:
        macro average precision: float as percent; rounded to two decimal points

    >>> precision(np.array([1,1,1,1,1,0]), np.array([0,0,1,1,1,1]))
    30.0

    >>> precision(np.array(['A','A','B','A', 'A', 'C', 'C']), np.array(['C','A','B','A', 'A', 'C', 'B']))
    75.0
    """
    pass

def recall(pred:np.array, true:np.array) -> float:
    """
    Input:
        pred: numpy array of predicted labels
        true: numpy array of true labels
    Output:
        macro average recall: float as percent; rounded to two decimal points

    >>> recall(np.array([1,1,1,1,1,0]), np.array([0,0,1,1,1,1]))
    37.5

    >>> recall(np.array(['A','A','B','A', 'A', 'C', 'C']), np.array(['C','A','B','A', 'A', 'C', 'B']))
    66.67
    """
    pass


def fscore(pred, true, f_val):
    """
    Input:
        pred: numpy array of predicted labels
        true: numpy array of true labels
    Output:
        macro average f-score: float; rounded to two decimal points

    >>> fscore(np.array(['A','A','B','A', 'A', 'C', 'C']), np.array(['C','A','B','A', 'A', 'C', 'B']), f_val=1)
    0.67

    >>> fscore(np.array(['A','A','B','A', 'A', 'C', 'C']), np.array(['C','A','B','A', 'A', 'C', 'B']), f_val=0.5)
    0.71

    >>> fscore(np.array([1,1,1,1,1,0]), np.array([0,0,1,1,1,1]), f_val=2)
    0.36
    """

def euclidean_distance(point: np.array, data: np.array) -> np.array:
    """ Calculates the euclidean distance for a point against all the data.

    Args:
        point (np.array): A single sample from test data
        data (np.array): All of the train data to calculate the distance for
    Returns:
        np.array: Distances between the point and all the data

    >>> euclidean_distance(np.array([0,0]), np.array([[3,3], [1,2], [2,1], [-3,-3]]))
    array([4.24264069, 2.23606798, 2.23606798, 4.24264069])
    
    >>> euclidean_distance(np.array([3,5,1]), np.array([[2,3,4], [3,5,2], [5,-1,0], [0,0,0]]))
    array([3.74165739, 1.        , 6.40312424, 5.91607978])
    """
    pass


def mode(labels: np.array) -> list:
    """ Returns the mode value from a list 

    Args:
        labels (list): A list of labels
    Returns:
        List of values that are the mode. List should have one value if there is only one mode. 

    >>> mode(['cat', 'dog', 'cat', 'butterfly'])
    ['cat']

    >>> mode(['cat', 'dog', 'cat', 'butterfly', 'dog'])
    ['cat', 'dog']


    >>> mode([1, 0, 0, 1, 2, 3, 3, 3])
    [3]

    >>> mode([1, 0, 0, 1, 2, 3])
    [0, 1]
    """ 
    pass



if __name__ == '__main__':
    doctest.testmod(verbose=True)
    