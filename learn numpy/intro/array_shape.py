import numpy as np

separator = '=' * 50

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)
print(separator)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array:', arr.shape)
print(separator)
