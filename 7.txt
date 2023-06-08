# 2
def main(x):
    x1 = str(hex(0b1111111 & x))
    x2 = str(hex(0b11111 & (x >> 7)))
    x3 = str(hex(0b111111 & (x >> 12)))
    x4 = str(hex(0b111111111 & (x >> 18)))
    dic = {
         'X1': x1,
         'X2': x2,
         'X3': x3,
         'X4': x4
     }
    return dic

print(main(55821475))



# 3
def main(s):
    l2 = int(s['L2'], 16)
    l3 = int(s['L3'], 16)
    l4 = int(s['L4'], 16)
    l5 = int(s['L5'], 16)
    l6 = int(s['L6'], 16)

    d = (l2 << 1) | (l3 << 10) | (l4 << 11) | (l5 << 13) | (l6 << 23)

    return d

print(main({'L2': '0x7a', 'L3': '0x1', 'L4': '0x3', 'L5': '0x3d8', 'L6': '0x2e'}))


# 4
def main(x):
    x = int(x, 16)
    l1 = str(hex(0b111111 & x))
    l2 = str(hex( 0b11111 & (x >> 6)))
    l3 = str(hex( 0b11111 & (x >> 11)))
    l4 = str(hex( 0b1111111111 & (x >> 16)))
    l5 = str(hex( 0b1 & (x >> 26)))
    l6 = str(hex( 0b1111111 & (x >> 27)))
    li = [('L1', l1), ('L2', l2), ('L3', l3), ('L4', l4), ('L5', l5), ('L6', l6)]
    return li

print(main('0x22899895a'))




# 5
def main(x):
    r1 = int(x[0], 16)
    r2 = int(x[1], 16)
    r4 = int(x[2], 16)

    return str(hex(r1 | (r2 << 9)| (r4 << 17)))


print(main(('0x1c3', '0x0', '0xa2')))




# 6
def main(x):
    x = int(x)
    d1 = 0b11111111 & x
    d2 = 0b1111111 & (x >> 8)
    d3 = 0b1111 & (x >> 15)
    d4 = 0b11 & (x >> 19)
    d6 = 0b1111 & (x >> 28)
    return tuple(map(str, (d1, d2, d3, d4, d6)))


print(main('589468639'))




# 7
def main(x):
    x = int(x)
    v1_1 = 0b1111111111 & x
    v2_1 = 0b111111111 & (x >> 10)
    v3_1 = 0b11 & (x >> 19)
    v4_1 = 0b11111 & (x >> 21)

    return (v1_1 | (v2_1 << 12) | (v3_1 << 10) | (v4_1 << 21))


print(main('39422957'))



