import math


def f(n):
    if n == 0:
        return 0.44
    if n >= 1:
        return math.pow((0.03+math.pow(f(n-1), 3)), 2) - math.ceil(f(n-1))


print(f(5))