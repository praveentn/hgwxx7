# matplotlib

import numpy as np
import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt


l = list(range(1,101))

plt.plot(l)
plt.ylabel('Non-negative Integers')
plt.show()

squared = list(map(lambda x:x*x, l))

plt.plot(l, squared)
plt.show()


# red circle or dots
# x-axis: 0 - 100
# y-axis: 0 - 10000
plt.plot(l, squared, 'ro')
plt.figure(1, figsize=(9, 3), linewidth=0.2)
plt.axis([0, 100, 0, 10000])
plt.show()


plt.plot(l, squared, 'b^')
plt.figure(1, figsize=(11, 23))
plt.axis([0, 100, 0, 10000])
plt.show()


data = {'a': np.arange(75),
        'c': np.random.randint(0, 75, 75),
        'd': np.random.randn(75)}
data['b'] = data['a'] + 10 * np.random.randn(75)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()


# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


names = ['group_a', 'group_b', 'group_c', 'group_d', 'group_c', 'group_b', 'group_a']
values = [1, 10, 100, 500, -250, -50, 1,]

plt.figure(1, figsize=(9, 3), linewidth=2.0)

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()


