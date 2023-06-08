import math


def f(y):
    s = 0
    n = len(y)
    y = [0] + y
    for i in range(1, n+1):
        s += math.pow((math.pow(y[n+1-i], 3) + y[n+1-math.ceil(i/4)]), 3) * 93
    return s * 8


print(f([-0.82, -0.34, -0.13]))