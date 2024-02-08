import numpy as np

sep = '=' * 50

arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)
print(newarr)
print(sep)

newarr = np.diff(arr, n=2)
print(newarr)
print(sep)

newarr = np.diff(arr, n=3)
print(newarr)
print(sep)

newarr = np.diff(arr, n=4)
print(newarr)
print(sep)
