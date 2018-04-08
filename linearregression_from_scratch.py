import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
from matplotlib import style
style.use('bmh') 

x=np.array([1,2,5,4,7,8,9],dtype=np.float64)
y=np.array([5,4,8,7,6,3,4],dtype=np.float64)

def best_fit_slope(x,y):
    m=(((mean(x)*mean(y)) -(mean(x*y))) /((mean(x)**2)-(mean(x**2))))      #slope for best fit line
    return m
m=best_fit_slope(x,y)
def best_fit_intercept(x,y):
    b=(mean(y)-(m*mean(x)))
    return b
b=best_fit_intercept(x,y)
print(m, b)

regression_line=[((m*x)+b) for x in x]

plt.scatter(x,y)
plt.plot(x,regression_line)
plt.show()
