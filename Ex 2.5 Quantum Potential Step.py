#Exercise 2.5: Quantum Potential Step

import numpy as np

V = float(input("Enter the height of potential step in electron volts = "))
E = float(input("Enter the value of energy in electron volts = "))
m = float(input("Enter the mass in kgs = "))
#V=9eV, E=10eV, m=9.11x10**(-31)kg

h_cut = 6.58e-16
k1 = np.sqrt(2*m*E)/h_cut
k2 = np.sqrt(2*m*(E-V))/h_cut

T = (4*k1*k2)/(k1+k2)**2
R = ((k1-k2)/(k1+k2))**2

print("Transmission Probability T = ", T)
print("Reflection Probability R = ", R)
