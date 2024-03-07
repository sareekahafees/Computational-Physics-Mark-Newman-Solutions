#converting polar coordinates
'''Suppose the position of a point in two-dimensional space is given to us in polar
coordinates r and theta, and we want to convert it to Cartesian coordinates x, y. How
would we write a program to do this? The appropriate steps are:
1. Get the user to enter the values of rand e.
2. Convert those values to Cartesian coordinates using the standard formulas:
x = rcose, y = rsine. (2.1)
3. Print out the results.'''

import numpy as np
r = float(input("Enter r = "))
d = float(input("Enter angle theta in degrees = "))

#convert degrees to radians as numpy takes sine and cosine in radians
theta = d*np.pi/180.0
x = r*np.cos(theta)
y = r*np.sin(theta)

print("x =", x, "y =", y)
