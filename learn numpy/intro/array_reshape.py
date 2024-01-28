import numpy as np

separator = '=' * 50

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
print(separator)

newarr = arr.reshape(2, 3, 2)
print(newarr)
print(separator)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
try:
    newarr = arr.reshape(3, 3)
    print(newarr)
except ValueError as e:
    print(e)
try:
    newarr = arr.reshape(2, 3)
    print(newarr)
except ValueError as e:
    print(e)
print(separator)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = arr.reshape(2, 4)
print(x.base)
y = x.copy()
print(y.base)
print(separator)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)
print(separator)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
try:
    newarr = arr.reshape(2, 3, -1)
    print(newarr)
    print(separator)
except ValueError as e:
    print(e)
print(separator)

lst = [[1, 2, 3], [4, 5, 6]]
arr = np.array(lst)
newarr = arr.reshape(-1)
print(newarr)
print(separator)

flattened = arr.flatten('C')
print('flattened C:', flattened)
print(flattened.base)
flattened = arr.flatten('F')
print('flattened F:', flattened)
print(flattened.base)
flattened = arr.flatten('A')
print('flattened A:', flattened)
print(flattened.base)
flattened = arr.flatten('K')
print('flattened K:', flattened)
print(flattened.base)
print(separator)

