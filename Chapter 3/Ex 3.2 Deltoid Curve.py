#plot of the deltoid curve defined parametrically by the equations
# x = 2cos(theta)+cos(2*theta)
# y = 2sin(theta) - sin(2*theta) where 0 <= theta <= 2pi

import numpy as np
import pylab as plt

theta = np.linspace(0,2*np.pi,100)
x = 2*np.cos(theta)+np.cos(2*theta)
y = 2*np.sin(theta)-np.sin(2*theta)

plt.plot(x,y)
plt.xlabel(r"$2cos(\theta) + cos(2\theta)$")
plt.ylabel(r"$2sin(\theta) - sin(2\theta)$")
plt.title('Deltoid Curve')
plt.show()
