import sympy as sp

t = sp.Symbol('t')
x = t ** 3 / 3 + sp.cos(t / 4) - t / 2
print(f'x(t) = {x}')

x_prime = sp.diff(x, t)
print(f"dx(t) / dt = {x_prime}")


# after isolating t for the equation t=g(t) :
def g(t):
    return float(sp.sqrt(0.5 + sp.sin(t / 4) / 4))


T = [1]  # t0
for i in range(1, 81):
    t_new = g(T[i - 1])
    T.append(t_new)
    if x_prime.subs(t, t_new) == 0:
        break

print(f'at t = {T[-1]}, dx(t)/dt = 0 with {i} times repetition.')
print(f'the particle passes {x.subs(t, T[-1])}m when it reaches the extremum of its motion.')
