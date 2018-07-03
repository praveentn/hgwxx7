import tkinter as tk
import numpy as np
import pylab
import scipy.stats as stats
from urllib.request import urlopen
import sys

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data = urlopen(target_url)
print(type(data))
print(data)

content =  data.read().decode(data.headers.get_content_charset())
print(type(content))

f = open("ml_sonar_1_.csv", "w")
f.write(content)
f.close()

#arrange data into list for labels and list of lists for attributes
xList = []
labels = []
with open("ml_sonar_1_.csv", "r") as r:
    for line in r.readlines():
        #split on comma
        row = line.strip().split(",")
        xList.append(row)

nrow = len(xList)
ncol = len(xList[1])

type = [0]*3
colCounts = []

#generate summary statistics for column 3 (e.g.)
col = 3
colData = []
for row in xList:
    #print(row)
    colData.append(float(row[col]))
stats.probplot(colData, dist="norm", plot=pylab)
pylab.show()
