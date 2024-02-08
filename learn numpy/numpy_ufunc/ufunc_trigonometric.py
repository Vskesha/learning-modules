import numpy as np

sep = '=' * 50

x = np.sin(np.pi / 2)
print(x)
print(sep)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
newarr = np.sin(arr)
print(newarr)
print(sep)

arr = np.array([90, 180, 270, 360])
newarr = np.deg2rad(arr)
print(newarr)
print(sep)

pi = np.pi
arr = np.array([pi/2, pi, 1.5 * pi, 2 * pi])
newarr = np.rad2deg(arr)
print(newarr)
print(sep)

x = np.arcsin(1.0)
print(x)
print(sep)

arr = np.array([1.0, -1.0, 0.1])
x = np.rad2deg(np.arcsin(arr))
print(x)
print(sep)

base = 3
perp = 4
hypotenues = np.hypot(base, perp)
print(hypotenues)
print(sep)
