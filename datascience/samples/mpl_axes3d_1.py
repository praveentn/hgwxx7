import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

fig = plt.figure()
ax = Axes3D(fig)

x_vals = np.random.rand(1000)
y_vals = np.random.rand(1000)
z_vals = np.random.rand(1000)

ax.scatter(x_vals, y_vals, z_vals, color='red')
ax.scatter(x_vals+0.3, y_vals-0.7, z_vals, color='blue')
ax.scatter(x_vals-0.3, y_vals+0.7, z_vals, color='green')

plt.show()
