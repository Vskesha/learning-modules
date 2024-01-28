import numpy as np

separator = '=' * 50
arr = np.array([1, 2, 3, 4, 5,])
print(arr)
print(type(arr))
print(separator)

arr = np.array((1, 2, 3, 4, 5))
print(arr)
print(separator)

# 0-D array
a = np.array(42)
print(a)
print(separator)

# 1-D array
b = np.array([1, 2, 3, 4, 5])
print(b)
print(separator)

# 2-D array
c = np.array([[1, 2, 3], [4, 5, 6]])
print(c)
print(separator)

# 3-D array
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(d)
print(separator)

# print arrays dimensions
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print(separator)

# set array dimension
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions:', arr.ndim)
print(separator)
