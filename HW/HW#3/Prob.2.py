# Gauss Seidel
x = y = z = w = 0

for i in range(3):
    x = (6 + y - 2 * z) / 10
    y = (25 + x + z - 3 * w) / 11
    z = (-11 - 2 * x + y + w) / 10
    w = (15 - 3 * y + z) / 8

    print(x, y, z, w)
