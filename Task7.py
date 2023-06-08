def main(bit_fields):
    result = 0
    result |= int(bit_fields[0][1])
    result |= int(bit_fields[1][1]) << 10
    result |= int(bit_fields[2][1]) << 12
    return result

print(main([('H1', '233'), ('H3', '0'), ('H4', '109')]))