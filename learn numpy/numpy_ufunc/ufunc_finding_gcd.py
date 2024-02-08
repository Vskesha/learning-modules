import numpy as np

sep = '=' * 50

num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)
print(sep)

arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x)
print(sep)
