import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

theta_max = np.pi * 8
n = 1000
theta = np.linspace(0, theta_max, n)
ax.plot(theta, np.cos(theta), np.sin(theta))
plt.show()
