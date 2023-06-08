import math


def f(b, n, m):
    s1 = 0
    s2 = 0
    for c in range(1, n+1):
        for i in range(1, b+1):
            s1 += 97 * math.ceil(1 + 38*i) + 18 * i * i + math.pow(c, 21)
    for j in range(1, b+1):
        for k in range(1, m+1):
            s2 += 1 + math.pow(72*k*k+j*j*j +1, 4) + math.pow(k ,6)
    return s1 - s2


print(f(5, 5, 7))