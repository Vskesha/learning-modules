import pandas as pd
import matplotlib.pyplot as plt

date = pd.date_range('2024-02-01', freq='D', periods=8)
plt.rc('font', size=10)
plt.rc('xtick', labelsize=6)
plt.plot(
    date,
    [23, 17, 17, 16, 15, 14, 17, 20],
    label='day temperature',
    color='#FF5733',
    linestyle='--',
    linewidth=2,
    marker='D'
)
plt.plot(
    date,
    [19, 11, 16, 11, 10, 10, 11, 16],
    label='night temperature',
    color='#061358',
    linestyle='dashdot',
    linewidth=2,
    marker='^'
)
plt.ylim(0, 25)
plt.xlabel('Дата', fontsize='small', color='midnightblue')
plt.ylabel('Температура', fontsize='small', color='midnightblue')
plt.title('Температура в Козові', fontsize=15)
plt.legend()
plt.grid()
plt.show()
