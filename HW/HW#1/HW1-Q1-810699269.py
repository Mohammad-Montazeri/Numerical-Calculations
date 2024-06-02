import numpy as np


def factorial(x):
    fac = 1
    if x >= 1:
        for i in range(1, x + 1):
            fac = fac * i
    return fac


def exp_taylor(x, n):
    sum = 0
    for i in range(1, n + 1):
        sum += x ** (i - 1) / factorial(i - 1)
    return sum


# a)
x = 0.75  # the exponent
m = 5  # precision with m decimal points
e_assured = 0.5 * 10 ** (-m)
true_value = np.exp(x)
n = 1

while True:
    absolute_err = abs(true_value - exp_taylor(x, n))
    if absolute_err <= e_assured:
        print(f'{n} terms of taylor series is required to calculate exp(0.75)={exp_taylor(x, n):.5f}')
        break
    n += 1

# b)
ans = exp_taylor(np.pi / 3, 5)
print(f'exp(pi/3) = {ans:.5f}')

# another way to solve part a)
# n=1
# while True:
#     if x**n / factorial(n)<=e_assured:  # truncation err <= 0.5*10**(-5)
#         print(n, f'{exp_taylor(x,n):.5f}')
#         break
#     n+=1
