import matplotlib.pyplot as plt
import numpy as np


def factorial(x):
    fac = 1
    if x >= 1:
        for i in range(1, x + 1):
            fac = fac * i
    return fac


x = np.linspace(2, 6, 200)
f1 = x * np.sin(x)
n = [4, 6, 8]

fig, ax = plt.subplots(2, 3, sharey=True, figsize=(12, 7))  # figure to show the plots

# now producing f2 depending on what n is:
for i in [0, 1, 2]:
    f2 = 0
    for j in range(0, n[i] + 1):
        f2 += (-1) ** j * x ** (2 * j + 2) / factorial(2 * j + 1)

    delta = f2 - f1

    # visualizing the results in multiple subplots:
    ax[0, i].plot(x, f1, label='f1')
    ax[0, i].plot(x, f2, label='f2')
    ax[1, i].plot(x, delta, label='f2-f1')
    ax[0, i].set_title(f'n = {n[i]}')
    ax[0, i].legend()
    ax[1, i].legend()
    ax[0, i].grid()

plt.show()

# conclusion: the larger the n, the closer the f2 to f1
# in fact, f2 is the Taylor expansion of f1, and with n enlarging, more terms
# of the series is included in f2, thus it can predict f1 more accurately.
