import numpy as np


def my_add(x, y):
    return x + y


my_add = np.frompyfunc(my_add, 2, 1)
print(my_add([1, 2, 3, 4], [4, 5, 6, 7]))

print(type(np.add))
print(type(my_add))
print(type(np.concatenate))

try:
    print(type(np.blahblahblah))
except AttributeError as err:
    print(err)

if type(np.add) == np.ufunc:
    print("add is ufunc")
else:
    print("add is not ufunc")
