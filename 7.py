def main(x: str) -> dict:
    X: int = int(x, 16)
    D: dict = {}
    D['S1'] = hex(X & 0xf)
    D['S2'] = hex(X >> 4 & 0b1111111)
    D['S3'] = hex(X >> 11 & 0b1111111111)
    D['S4'] = hex(X >> 21 & 0b1111111)
    D['S6'] = hex(X >> 31 & 0b1)
    return D


print(main('0xa5fc49f'))
# {'S1': '0xf', 'S2': '0x49', 'S3': '0x3f8', 'S4': '0x52', 'S6': '0x0'}
# {'s1': '0xf', 's2': '0x49', 's3': '0x3f8', 's4': '0x52', 's6': '0x0'}
print(main('0xc2bee1a5'))
# {'S1': '0x5', 'S2': '0x1a', 'S3': '0x3dc', 'S4': '0x15', 'S6': '0x1'}
print(main('0x4db952d6'))
# {'S1': '0x6', 'S2': '0x2d', 'S3': '0x32a', 'S4': '0x6d', 'S6': '0x0'}
print(main('0x2fc9ef62'))
# {'S1': '0x2', 'S2': '0x76', 'S3': '0x13d', 'S4': '0x7e', 'S6': '0x0'}