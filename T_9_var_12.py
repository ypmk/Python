def main(args):
    result = []
    length = len(args)
    print(args)
    row_1 = []
    for i in range(0, length):
        if args[i][0] is not None:
            row_1.append((args[i][0].split('|')[0]).replace('-', '/'))
    result.append(row_1)

    row_2 = []
    for i in range(0, length):
        if args[i][0] is not None:
            row_2.append(args[i][1].split('@')[1])
    result.append(row_2)

    row_3 = []
    for i in range(0, length):
        if args[i][0] is not None:
            if args[i][0].split('|')[1] == 'N':
                row_3.append('нет')
            else:
                row_3.append('да')
    result.append(row_3)

    row_4 = []
    for i in range(0, length):
        if args[i][0] is not None:
            s = args[i][3].split('.')[0]
            s = s[0:-2]
            s += args[i][3].split('.')[1]
            row_4.append(s)
    result.append(row_4)

    return result

print(main([['2003-03-03|N', 'aleksandr72@yahoo.com', 'aleksandr72@yahoo.com', 'Александр К. Гочоций'],
            ['2000-06-14|N', 'tazesuk84@yandex.ru', 'tazesuk84@yandex.ru', 'Тихон Ф. Тазесук'],
            [None, None, None, None]]))
