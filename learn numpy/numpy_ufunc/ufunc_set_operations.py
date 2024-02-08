import numpy as np

sep = '=' * 50

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)
print(type(x))
print(sep)

arr1 = np.array([3, 4, 1, 2])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)
print(newarr)
print(sep)

newarr = np.intersect1d(arr1, arr2, assume_unique=True)
print(newarr)
print(sep)

newarr = np.setdiff1d(arr1, arr2, assume_unique=True)
print(newarr)
print(sep)

newarr = np.setxor1d(arr1, arr2, assume_unique=True)
print(newarr)

