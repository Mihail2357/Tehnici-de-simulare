import numpy as np
from scipy import integrate
import math


def exponential():
    N = 0
    while True:
        u0 = np.random.uniform()
        u1 = np.random.uniform()
        u = u0
        k = 1
        while u0 >= u1:
            k += 1
            u0 = u1

            u1 = np.random.uniform()

        if k % 2 == 1:
            return N + u
        else:
            N += 1


def Gama(v):
    x2 = lambda x: (x ** (v - 1)) * np.exp(-x)
    p1 = integrate.quad(x2, 0, 1)[0] / integrate.quad(x2, 0, np.inf)[0]
    p2 = 1 - p1
    U = np.random.uniform()
    if p1 <= U:
        # generam X1
        k = 0
        while k % 2 == 0:
            U1 = np.random.uniform()
            Z0 = U1 ** (1 / v)
            Z1 = np.random.uniform()
            k = 1
            Zstar = Z0

            while Z0 >= Z1:
                Z0 = Z1
                Z1 = np.random.uniform()
                k += 1

            if k % 2 == 1:
                X1 = Zstar
                return X1

    else:
        # generam x2
        Y = np.inf
        Z = 0
        while Y > Z:
            U2 = np.random.uniform()
            Z = U2 ** (-1 / (1 - v))
            X0 = exponential()
            Y = X0 + 1

        return Y


def pascal1(k, p):
    x = 0
    j = 0
    while j < k:
        y = np.random.uniform()
        if y < p:
            j += 1
        else:
            x += 1

    return x


def pascal2(k, p):  # metoda inversa
    q = 1 - p
    U = np.random.uniform()
    s = 0
    x = 0
    while s < U:
        P = 1
        for i in range(x + 1, x + k):
            P *= i
        P = P / math.factorial(k - 1)

        for i in range(k):
            P *= p

        for i in range(x):
            P *= q

        s += P
        x += 1

    return x - 1


nrsimulations = 1000
#v=float(input())
v = np.random.uniform()
Gamasimulations = [Gama(v) for i in range(nrsimulations)]
print("Variabila Gama: ")
print("Media: ", np.mean(Gamasimulations))
print("Dispersia: ", np.var(Gamasimulations))
print('\n')

print("Variabila Pascal cu metoda 1: ")
k=10
p = np.random.uniform()
pascal = [pascal1(k, p) for i in range(nrsimulations)]
print("Media: ", np.mean(pascal))
print("Dispersia: ", np.var(pascal))

print('\n')
print("Variabila Pascal cu metoda 2: ")
#p = np.random.uniform()
pascal = [pascal2(k, p) for i in range(nrsimulations)]
print("Media: ", np.mean(pascal))
print("Dispersia: ", np.var(pascal))

print('\n')
print("Media teoretica Pascal: ",k*(1-p)/p )
print("Dispersia teoretica Pascal: ",k*(1-p)/p/p )


