import math


def main(n):
    x = 0.26
    y = -0.17
    for i in range(n - 1):
        v = y - math.ceil(x) ** 2
        x = y
        y = v
    return y