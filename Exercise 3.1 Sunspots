import numpy as np
import pylab as plt

data = np.loadtxt('sunspots.txt', float)
x = data[:1001,0]
y = data[:1001,1]

for r in range(-5,5,1):
    yk = y + r
    Yk = (1/(2*r+1))*yk

plt.plot(x,y)
plt.plot(x,Yk)
plt.xlabel('x = month')
plt.ylabel('y = no. of sunspots')
plt.xlim(0,1000)
plt.show()
