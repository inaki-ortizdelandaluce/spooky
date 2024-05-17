import numpy as np


def null_or_empty(arr):
    return arr is None or (isinstance(arr, np.ndarray) and not arr.size)
