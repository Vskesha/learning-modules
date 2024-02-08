from functools import partial
from math import log

import numpy as np

sep = '=' * 50

arr = np.arange(1, 10)
print(np.log2(arr))
print(sep)

print(np.log10(arr))
print(sep)

print(np.log(arr))
print(sep)

nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))
print(sep)


def log15(x):
    return log(x, 15)


log15 = np.frompyfunc(log15, 1, 1)
print(log15(100))
print(type(log15))
print(sep)
