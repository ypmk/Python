def main(x):
     e = x & (0b1 << 31)
     d = x & (0b11111 << 26)
     c = x & (0b1111 << 22)
     b = x & (0b111111111 << 13)
     a = x & 0b1111111111111

     return (d >> 13) | (b >> 13) | (e >> 13) | (a << 19) | (c >> 13)

print(hex(main('0x43a72b')))
print(hex(main('0x7a7c29')))
print(hex(main('0x7e1df9')))
print(hex(main('0x51d645')))
