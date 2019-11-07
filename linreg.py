#@author Max Schaefer
#Linear Regression


#from bokeh.plotting import figure, show
#from bokeh.models import Slope
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
sns.set_style("darkgrid")

import plotly.express as px


###########helper functions###########
def mean(arr):
    return sum(arr)/len(arr)

def productsum(arr1, arr2):
    if(len(arr1) == len(arr2)):
        sum = 0
        for i in range(len(arr1)):
            sum += arr1[i] * arr2[i]
        return sum
    else:
        return 0

##########import data##########
f = open("data2.txt")

points = []
for line in f:
    point = line.split("\t")
    point = [float(component.strip()) for component in point]
    points.append(point)

xarr = []
yarr = []
for point in points:
    if(len(point) == 2):
        xarr.append(point[0])
        yarr.append(point[1])

##########Regression Calculations###########

mtop = (productsum(xarr, yarr)) - (mean(yarr) * mean(xarr) * len(xarr))
mbottom = productsum(xarr, xarr) - (len(xarr)*(mean(xarr)**2))
m = ( mtop ) / (mbottom)
b = mean(yarr) - (m * mean(xarr))

ypred = lambda x : (m * x) + b

print("Lin Reg: y = " + str(m) + "x + " + str(b))

##########plot data##########
linex = np.linspace(min(xarr), max(xarr), 2)
liney = [ypred(x) for x in linex]

#bokeh plot
#p = figure(plot_width=400, plot_height=400)
#p.circle(xarr, yarr, size=8, color="navy", alpha=0.5)
#slope = Slope(gradient=m, y_intercept=b, line_color='red', line_dash='dashed', line_width=4)
#p.add_layout(slope)
#show(p)


#matplotlib/seaborn
plt.scatter(xarr, yarr)
plt.plot(linex,liney)
plt.show()

