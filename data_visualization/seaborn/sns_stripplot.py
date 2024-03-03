import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("mpg")
sns.set_style("darkgrid")

sns.stripplot(data=data, x='origin', y='mpg', hue='origin')
plt.show()
