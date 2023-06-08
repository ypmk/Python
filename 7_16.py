def main(x):
    x = int(x)

    g1mask = 0b1111111
    g2mask = 0b1110000000
    g3mask = 0b11111111110000000000

    dic = {
        'G1': g1mask & x,
        'G2': (g2mask & x) >> 7,
        'G3': (g3mask & x) >> 10,
    }

    return dic

print(main('182697'))