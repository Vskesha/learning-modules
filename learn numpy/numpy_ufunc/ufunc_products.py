import numpy as np

sep = '=' * 50

arr = np.array([1, 2, 3, 4])
x = np.prod(arr)
print(x)
print(sep)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

x = np.prod([arr1, arr2])
print(x)
print(sep)

newarr = np.prod([arr1, arr2], axis=0)
print(newarr)
print(sep)

newarr = np.prod([arr1, arr2], axis=1)
print(newarr)
print(sep)

newarr = np.cumprod(arr2)
print(newarr)
print(sep)
