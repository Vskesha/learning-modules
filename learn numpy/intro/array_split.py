import numpy as np

separator = '=' * 50

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)
print(separator)

newarr = np.array_split(arr, 4)
print(newarr)
print(type(newarr))
print(type(newarr[0]))
print(separator)

newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])
print(separator)

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)
print(separator)

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [10, 11, 12],
                [13, 14, 15],
                [16, 17, 18]])
newarr = np.array_split(arr, 3)
print(newarr)
print(separator)

newarr = np.array_split(arr, 3, axis=1)
print(newarr)
print(separator)

newarr = np.hsplit(arr, 3)
print(newarr)
print(separator)

newarr = np.vsplit(arr, 3)
print(newarr)
print(separator)

