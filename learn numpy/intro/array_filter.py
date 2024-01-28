import numpy as np

separator = '=' * 50

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)
print(separator)

filter_arr = [element > 42 for element in arr]
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
print(separator)

arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = [not element % 2 for element in arr]
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
print(separator)

arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
print(separator)

arr = np.arange(1, 8)
print(arr)
print(type(arr))
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
print(separator)
