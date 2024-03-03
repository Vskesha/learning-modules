import seaborn as sns
from matplotlib import pyplot as plt

data = sns.load_dataset("mpg")
sns.set_style("darkgrid")
# print(type(data))
# print(data.head())
# print(data.columns.values)
# print(type(data.columns.values))

sns.lineplot(data=data, x="model_year", y="horsepower", hue="origin")
plt.show()
