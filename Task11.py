import struct
import pprint


def parse_e(data, pointer):
    e1 = struct.unpack('>Q', data[pointer:pointer + 8])[0]
    e2 = list(struct.unpack('>3b', data[pointer + 8:pointer + 11]))
    e3 = struct.unpack('>B', data[pointer + 11:pointer + 12])[0]
    return {'E1': e1, 'E2': e2, 'E3': e3}


def parse_d(data, pointer):
    d1, d2, d3, d4 = list(struct.unpack('>fIih', data[pointer:pointer + 14]))
    d5, d6, d7, d8 = list(struct.unpack('>fhQd',
                                        data[pointer + 14:pointer + 36]))
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4,
            'D5': d5, 'D6': d6, 'D7': d7, 'D8': d8}


def parse_c(data, pointer):
    c1 = struct.unpack('>b', data[pointer:pointer + 1])[0]
    c2 = list(struct.unpack('>2h', data[pointer + 1:pointer + 5]))
    return {'C1': c1, 'C2': c2}


def parse_b(data, pointer):
    b1, b2, b3, b4 = list(struct.unpack('>QbbB', data[pointer:pointer + 11]))
    b5 = list()
    f5 = struct.unpack('>7I', data[pointer + 11:pointer + 39])
    for i in range(7):
        b5.append(parse_c(data, f5[i]))
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4,
            'B5': b5}


def parse_a(data, pointer):
    a1 = ''.join(map(str, struct.unpack('>8c',
                                        data[pointer:pointer + 8])))
    a1 = a1.replace('\'', '')[1::2]
    f2 = struct.unpack('>I', data[pointer + 8:pointer + 12])[0]
    a2 = parse_b(data, f2)
    f3 = struct.unpack('>H', data[pointer + 12:pointer + 14])[0]
    a3 = parse_d(data, f3)
    f4 = struct.unpack('>I', data[pointer + 14:pointer + 18])[0]
    a4 = parse_e(data, f4)
    a5, a6 = list(struct.unpack('>bQ', data[pointer + 18:pointer + 27]))
    f7 = struct.unpack('>II', data[pointer + 27:pointer + 35])
    a7 = list(struct.unpack(f'>{f7[0]}d', data[f7[1]:f7[1] + f7[0] * 8]))
    a8 = struct.unpack('>f', data[pointer + 35:pointer + 39])[0]
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7, 'A8': a8}


def main(data):
    return parse_a(data, 4)


# Testing
pprint.pprint(main(b'MBUAjoarbobh\x00\x00\x00N\x00u\x00\x00\x00\x99\xdac\xbdV\x087\x1c\xcfw\x00'
 b'\x00\x00\x02\x00\x00\x00\xa5\xbe[\xea[>\x13&\xd00\xeaeO\xd5n\xb3r\xb6\x12iHW'
 b'*\xb5\xb7\x9cke\xd9\xa0\xd9\xe4\xe4\x0bA\xc9\xd0v\x91\xa7\xb9\x90'
 b's\x08\xc4\x8ac\xcd\xcf\xa3\xd4\x00\x00\x00+\x00\x00\x000\x00\x00\x00'
 b'5\x00\x00\x00:\x00\x00\x00?\x00\x00\x00D\x00\x00\x00I\xbf$\xd2'
 b'\xc8\x00\xce\x9a\x04h\x9f\xc2\xd9\x04\xbb\xbfjM\x0b\xe7A\x03\xb6\xcd'
 b'\xb7\x87\xd7\xbcw?\xe1\x1a\xc6\xf7T6\xd4\xf5\x80\xe3\xea\x99\x90s)\xdbj\xf1'
 b'\x93\xbf\xed#O\xcb\x8c!\xb8?\xef^\xb7\xc6\x91y`'))
