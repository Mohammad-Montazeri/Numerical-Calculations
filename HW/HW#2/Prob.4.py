import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x')
A = np.linspace(1, 4, 100)


def f(x):
    return float(x ** 3 - a * sp.exp(x) + x)


def f_prime(t):
    dif = sp.diff(x ** 3 - a * sp.exp(x) + x, x)
    return float(dif.subs(x, t))


roots = []

for i in range(100):
    a = A[i]
    X = [1]  # x0
    for j in range(1, 11):
        x_new = X[j - 1] - f(X[j - 1]) / f_prime(X[j - 1])
        X.append(x_new)

    roots.append(x_new)

plt.plot(A, roots)
plt.ylabel('x (root)')
plt.xlabel('a')
plt.grid()
plt.show()
