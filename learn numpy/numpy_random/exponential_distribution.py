from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.exponential(scale=2, size=(2, 3))
print(x)

sns.distplot(random.exponential(size=1000), hist=False)
plt.show()
