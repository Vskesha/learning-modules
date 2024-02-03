import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

separator = "=" * 50

x = np.random.normal(size=(2, 3))
print(x)
print(separator)

x = np.random.normal(loc=1, scale=2, size=(2, 3))
print(x)
print(separator)

sns.distplot(np.random.normal(size=1000), hist=False)
plt.show()

