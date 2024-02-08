import numpy as np

sep = '=' * 50

num1 = 4
num2 = 6

x = np.lcm(num1, num2)
print(x)
print(sep)

arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x)
print(sep)

arr = np.arange(1, 11)
x = np.lcm.reduce(arr)
print(x)
print(sep)
