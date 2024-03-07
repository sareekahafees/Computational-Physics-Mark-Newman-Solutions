#Exercise 2.6 Planetary Orbits
'''Write a program that asks the user to enter the distance to the Sun and velocity
at perihelion, then calculates and prints the quantities e2 , v2, T, and e.'''
#semi-major axis: a, semi-minor axis: b, orbital period: T, orbital eccentricity: e, 
#planetary mass: m, sun's mass: M, perihelion distance: L1, aphelion distance: L2

import numpy as np

L1 = float(input("Enter the distance to the planet from the sun = "))
v1 = float(input("Enter the velocity of the planet at perihelion = "))

G = 6.6378e-11
M = 1.9891e30

v2 = ((G*M)/(v1*L1))-np.sqrt(((G*M)/(v1*L1))**2-((2*G*M)/L1)+(v1**2))
print(v2)

L2 = L1*v1/v2

a = 0.5*(L1+L2)
b = np.sqrt(L1*L2)
T = ((2*np.pi*a*b)/(L1*v1))/(60*60*24*365)
e = (L2-L1)/(L2+L1)

print("The distance L2 at aphelion is = ", L2)
print("The velocity v2 at aphelion is = ", v2)
print("The orbital period T is = ", T)
print("The orbital eccentricity e is = ", e)
