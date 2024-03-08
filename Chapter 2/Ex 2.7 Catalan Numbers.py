'''The Catalan numbers C,, are a sequence of integers 1, 1, 2, 5, 14, 42, 132 ... that play
an important role in quantum mechanics and the theory of disordered systems.
Write a program that prints, in increasing order, all Catalan numbers less than or equal
to one billion.'''
#C_zero = 1

C_n = 1
n = 0
while C_n <= 10e9:
    C_n = (((4*n)+2)*C_n)/(n+2)
    n += 1
    print(C_n)