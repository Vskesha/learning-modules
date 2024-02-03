from numpy import random
from matplotlib import pyplot as plt
from seaborn import distplot

x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)

# distplot(random.logistic(size=1000), hist=False)
# plt.show()

distplot(random.normal(scale=2, size=1000), hist=False)
distplot(random.logistic(size=1000), hist=False)
plt.show()
