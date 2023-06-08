import math


def f(n):
    if n == 0:
        return 0.94
    if n == 1:
        return 0.37
    if n >= 2:
        return math.pow(math.log((81 * math.pow(f(n-1), 3) + 10 * math.pow(f(n-2), 2)), 10), 3)


print(f(4))