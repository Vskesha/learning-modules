import numpy as np

separator = '=' * 50

arr = np.array([1, 2, 3, 4])
print(arr.dtype)
print(separator)

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)
print(separator)

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)
print(separator)

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)
print(separator)

arr = np.array(['2', '3'], dtype='i')
print(arr)
print(arr.dtype)
print(separator)

arr = np.array([1.1, 2.1, 3.1])
print(arr)
print(arr.dtype)
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)
print(separator)

arr = np.array([1.1, 2.1, 3.1])
print(arr)
print(arr.dtype)
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)
print(separator)

arr = np.array([1, 0, 3])
print(arr)
print(arr.dtype)
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)
print(separator)
