import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

x = [5, 10, 15, 20]
y = [10, 0, 5, 15]
z = [0, 10, 5, 25]
s = [150, 300, 30, 160]

ax.scatter(x, y, z, s=s)
plt.show()
