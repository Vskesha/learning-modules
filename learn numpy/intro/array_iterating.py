import numpy as np

separator = '=' * 50

arr = np.array([1, 2, 3])
for x in arr:
    print(x)
print(separator)

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print(x)
print(separator)

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    for y in x:
        print(y)
print(separator)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    print(x)
print(separator)

for x in arr:
    for y in x:
        for z in y:
            print(z)
print(separator)

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)
print(separator)

arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)
print(separator)

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
for x in np.nditer(arr[:, ::2]):
    print(x)
print(separator)

arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)
print(separator)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)
print(separator)
