import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
plt.xlabel('x axis', fontsize=16)
plt.ylabel('y axis', fontsize=16)

grid = np.linspace(-10, 10, 40)
x, y = np.meshgrid(grid, grid)
z = x ** 2 * y ** 2 + 2

ax.plot_surface(x, y, z)
plt.show()
