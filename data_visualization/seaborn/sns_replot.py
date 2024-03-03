import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("mpg")
sns.set_style("darkgrid")

sns.relplot(data=data, x='mpg', y='displacement', kind='scatter', hue='origin', col='origin')
plt.show()
