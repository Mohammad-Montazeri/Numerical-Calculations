import numpy as np
import matplotlib.pyplot as plt

x = [1, 5, 10, 12, 15, 20, 35, 42]
y = [10, 50, 120, 194, 250, 281, 302, 368]
x2 = [i ** 2 for i in x]
xy = [x[i] * y[i] for i in range(len(x))]
n = len(x)

# linear regression
# y = P(x) = ax + b

sigma = lambda t: sum(t)
average = lambda t: sum(t) / len(t)

a = (n * sigma(xy) - sigma(x) * sigma(y)) / (n * sigma(x2) - sigma(x) ** 2)
b = average(y) - a * average(x)

print(f'a = {round(a, 4)} \t and \t b = {round(b, 4)}')

X = np.arange(0.5, 42.5, 0.5)
Y = a * X + b

plt.plot(X, Y, 'r', label='Regression')
plt.scatter(x, y, marker='o', label='Data')
plt.legend()
plt.show()
