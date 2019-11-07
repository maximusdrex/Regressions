#@author Max Schaefer
#Linear Regression

from bokeh.plotting import figure, show
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
sns.set()
sns.set_style("darkgrid")


###########helper functions###########

# gets the mean of an array
def mean(arr):
    return sum(arr)/len(arr)

#
def arr2Sum(arr1, arr2, c1, c2):
    if(len(arr1) == len(arr2)):
        sum = 0
        for i in range(len(arr1)):
            sum += (arr1[i] ** c1) * (arr2[i] ** c2)
        return sum
    else:
        return 0

#
def arr1Sum(arr1, c1):
    sum = 0
    for i in arr1:
        sum += i ** c1
    return sum


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

###find matrices###

n = int(input("degree"))
mat1 = []
for i in range(n+1):
    row = arr2Sum(xarr, yarr, n-i, 1)
    mat1.append(row)
print(mat1)
print(str(len(mat1)) )

matr = np.array(mat1)

mat2 = []
for i in range(n+1):
    row = []
    for j in range(n+1):
        term = "a" + str(j + 1) + " * Sum(" + "xi ^ (" + str((n - i) + (n - j)) + "))"
        term = arr1Sum(xarr, (n-i) + (n-j))
        row.append(term)
    mat2.append(row)

print(mat2)
print(str(len(mat2)) + " " + str(len(mat2[0])) )

matl = np.array(mat2)

###calc regression###

matlinv = np.linalg.inv(matl)

regcoeff = np.matmul(matlinv, matr)

eqstr = ""
for i in range(n):
    eqstr += str(regcoeff[i]) + "x^" + str(n - i) + " + "
eqstr += str(regcoeff[n])
print(eqstr)

def ypred(x):
    sum = 0
    for i in range(n+1):
        sum += (regcoeff[i]* (x ** (n-i)))
    return sum

##########plot data##########

linex = np.linspace(min(xarr), max(xarr), 1000)
liney = [ypred(x) for x in linex]

#bokeh plot
#p = figure(plot_width=400, plot_height=400)
#p.circle(xarr, yarr, size=8, color="navy", alpha=0.5)
#p.line(linex, liney, line_width=2)


plt.scatter(xarr, yarr)
plt.plot(linex,liney)
plt.show()

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
"""