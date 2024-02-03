from numpy import random
import numpy as np

separator = "=" * 50

arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)
print(separator)

print(random.permutation(arr))
print(separator)
