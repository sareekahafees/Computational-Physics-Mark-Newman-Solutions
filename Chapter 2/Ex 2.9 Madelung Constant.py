'''Exercise 2.9: Madelung Constant
Write a program to calculate and print the Madelung constant for sodium chloride.'''

import numpy as np
e = -1.602e10-19
eps_naught = 8.854e10-12
a = 0.000000000564
V = 0.0
M = 0.0

for i in range(-10,10,1):
    for j in range(-10,10,1):
        for k in range(-10,10,1):
            if i == 0 and j == 0 and k == 0:
                continue
            elif abs(i+j+k)%2==0:
                V += e/((4*np.pi*eps_naught*a)*np.sqrt(i**2+j**2+k**2))
            else:
                V += -e/((4*np.pi*eps_naught*a)*np.sqrt(i**2+j**2+k**2))

M += V*4*np.pi*eps_naught*a/e
print("The Madelung constant M for sodium chloride is = ", abs(M))
