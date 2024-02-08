import numpy as np

sep = '=' * 50

arr = np.trunc([-3.1666, 3.6667])
print(arr)
print(sep)

arr = np.fix([-3.1666, 3.6667])
print(arr)
print(sep)

arr = np.around(3.1666, 2)
print(arr)
print(sep)

arr = np.around(31.666, 2)
print(arr)
print(sep)

arr = np.around([-3.1666, 3.6667], 2)
print(arr)
print(sep)

arr = np.floor([-3.1666, 3.6667])
print(arr)
print(sep)

arr = np.ceil([-3.1666, 3.6667])
print(arr)
print(sep)
