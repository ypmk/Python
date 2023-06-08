import math


def f(n):
    if n == 0:
        return -0.62
    if n == 1:
        return 0.56
    if n >= 2:
        return math.pow(f(n-2), 2) - f(n-1) - 32


print(f(5))