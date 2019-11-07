#@author Max Schaefer
#Linear Regression

#from bokeh.plotting import figure, show
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
sns.set()
sns.set_style("darkgrid")


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
mtop = (productsum(xarr, yarr)) - (mean(yarr) * mean(xarr) * len(xarr))
mbottom = productsum(xarr, xarr) - (len(xarr)*(mean(xarr)**2))
m = ( mtop ) / (mbottom)
b = mean(yarr) - (m * mean(xarr))

ypred = lambda x : (m * x) + b

##########plot data##########

linex = np.linspace(min(xarr), max(xarr), 2)
liney = [ypred(x) for x in linex]

#bokeh plot
#p = figure(plot_width=400, plot_height=400)
#p.circle(xarr, yarr, size=8, color="navy", alpha=0.5)

#p.line(linex, liney, line_width=2)

#sns.relplot(x=xarr, y=yarr)
plt.scatter(xarr, yarr)
plt.plot(linex,liney)
plt.show()
#show(p)

"""
psuedo-code implementation:
mat1 = mat2 * X
X = mat2inv * mat1
n = degree
np.matrix([[],[],...])

mat1 = []
for i in range(n+1):
    row = "Sum(" + "yi * (xi ^ " + str() + ")" + ")"
    mat.append(row)