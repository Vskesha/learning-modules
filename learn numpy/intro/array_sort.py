import numpy as np

separator = '=' * 50

arr = np.array([3, 2, 0, 1])
print(np.sort(arr))
print(separator)

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))
print(separator)

arr = np.array([True, False, True])
print(np.sort(arr))
print(separator)

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))
print(separator)
