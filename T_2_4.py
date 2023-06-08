import math


def f(y):
    if y < 33:
        a = math.pow(math.sin(17*y - y*y*y), 5)
        b = math.exp(y, 7)
        return 1 - a - b
    elif 33 <= y < 89:
        return 44 * math.cos(y*y)
    elif 89 <= y < 125:
        return math.pow(y, 7)
    elif y >= 125:
        a = (y*y)/81
        b = 11 * math.pow(y-76-56*y*y, 5)
        c = math.pow(math.floor(y*y), 4)
        return a - b - c


print(f(56))