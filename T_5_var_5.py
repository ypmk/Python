import math


def f(y, x, z):
    n = len(y)
    y = [0] + y
    x = [0] + x
    z = [0] + z
    s = 0
    for i in range(1, n+1):
        s += math.pow(math.cos(math.pow(z[math.ceil(i/3)], 3) + x[i] + math.pow(y[i], 2)), 2) / 61
    return 29 * s


print(f([0.34, -0.48, -0.68],
[-0.98, 0.32, -0.24],
[0.72, -0.34, 0.37]))