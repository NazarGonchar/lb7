from numpy import *
import matplotlib.pyplot as plt
import pylab

x = linspace(0,4)
y = sin(10*x)*sin(3*x)/(x**2)

plt.plot(x, y, 'r-', label = 'sin(10*x)*sin(3*x)/(x**2)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('My graph')
plt.legend(['sin(10*x)*sin(3*x)/(x**2)'],
        loc='upper left')

pylab.savefig('file2.png',dpi=200)
plt.show()