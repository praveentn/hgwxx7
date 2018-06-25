# pattern recognition

import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
from matplotlib import style
style.use("ggplot")

fn = lambda astr: mdates.strpdate2num('%Y%m%d%H%M%S')(astr.decode())

def graphRawFX():
    date,bid,ask = np.loadtxt('GBPUSD1d.txt', unpack=True, delimiter=',', converters={0:fn})

    fig = plt.figure(figsize=(10,7))

    ax1 = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)
    ax1.plot(date,bid)
    ax1.plot(date,ask)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    plt.subplots_adjust(bottom=.23)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
    plt.grid(True)
    plt.show()

graphRawFX()