def main(args):
    result = []
    for i in args:
        row = []
        if i[1] == '1':
            row.append('true')
        else:
            row.append('false')
        row.append(i[2].replace('-', '/'))
        row.append(i[3].split('@')[1])
        if row not in result:
            result.append(row)
    return result


# Testing
print(main([[None, '1', '24-02-03', 'rodusic5@mail.ru'], [None, '0', '05-09-00', 'facikak6@yahoo.com'], [None, '1', '24-02-03', 'rodusic5@mail.ru']]))
