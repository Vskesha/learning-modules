import numpy as np

separator = '=' * 50

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
print(separator)

print(arr[4:])
print(separator)

print(arr[:4])
print(separator)

print(arr[-3:-1])
print(separator)

print(arr[1:5:2])
print(separator)

print(arr[::2])
print(separator)

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])
print(separator)

print(arr[0:2, 2])
print(separator)

print(arr[0:2, 1:4])
print(separator)
