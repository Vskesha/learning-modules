import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("mpg")

# print(data.head())

sns.set_style("whitegrid")
date = pd.date_range(start="2024-03-05", freq="D", periods=8)
day = [23, 17, 17, 16, 15, 14, 17, 20]
night = [19, 11, 16, 11, 10, 10, 11, 16]
df = pd.DataFrame({
    'date': date,
    'day_temperature': day,
    'night_temperature': night
})
# sns.lineplot(data=df)
sns.lineplot(data=df, y="day_temperature", x="night_temperature", sort=False)
plt.show()
