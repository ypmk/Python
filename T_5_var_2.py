import math


def f(y, z, x):
    n = len(x)
    y = [0] + y
    z = [0] + z
    x = [0] + x
    s = 0
    for i in range(1, n+1):
        s += 37 * math.pow((9*math.pow(z[n+1-i], 2) + math.pow(x[i], 3) + y[n+1-i]), 6)
    return s