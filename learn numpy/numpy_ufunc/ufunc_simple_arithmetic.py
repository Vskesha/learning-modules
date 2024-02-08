import numpy as np

sep = '=' * 50

arr1 = np.array([11, 12, 13, 14, 15])
arr2 = np.array([21, 22, 23, 24, 25])
newarr = np.add(arr1, arr2)
print(newarr)
print(sep)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.subtract(arr1, arr2)
print(newarr)
print(sep)

newarr = np.multiply(arr1, arr2)
print(newarr)
print(sep)

arr2 = np.array([3, 5, 10, 8, 2, 33])
newarr = np.divide(arr1, arr2)
print(newarr)
print(sep)

arr2 = np.array([3, 5, 6, 8, 2, 33])
newarr = np.power(arr1, arr2)
print(newarr)
print(sep)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.mod(arr1, arr2)
print(newarr)
print(sep)

newarr = np.remainder(arr1, arr2)
print(newarr)
print(sep)

newarr = np.divmod(arr1, arr2)
print(newarr)
print(sep)

arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
print(newarr)
print(sep)
