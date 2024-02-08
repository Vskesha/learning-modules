import numpy as np

sep = '=' * 50


arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
print(arr1 is arr2)
newarr = np.add(arr1, arr2)
print(newarr)
print(sep)

newarr = np.sum([arr1, arr2])
print(newarr)
print(sep)

newarr = np.sum([arr1, arr2], axis=0)
print(newarr)
print(sep)

newarr = np.sum([arr1, arr2], axis=1)
print(newarr)
print(sep)

newarr = np.cumsum(arr1)
print(newarr)
print(sep)
