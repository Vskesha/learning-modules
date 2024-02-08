import numpy as np

sep = '=' * 50

x = np.sinh(np.pi / 2)
print(x)
print(sep)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
newarr = np.cosh(arr)
print(newarr)
print(sep)

x = np.arcsinh(1.0)
print(x)
print(sep)

arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)
print(x)
print(sep)
