import numpy as np

def main(args):
    result = []
    for i in args:
        row = []
        s = i[0].split(';')[1]
        row.append(s[0:-2])
        if i[2] == 'Выполнено':
            row.append('true')
        else:
            row.append('false')
        if (i[0].split(';')[0].split('.')[1])[0] == '0':
            row.append((i[0].split(';')[0].split('.')[1])[1]+'%')
        else:
            row.append(i[0].split(';')[0].split('.')[1]+'%')
        result.append(row)

    for i in range(0, len(result)-1):
        for j in range(len(result)-i-1):
            if result[j][0] > result[j+1][0]:
                t_0 = result[j][0]
                t_1 = result[j][1]
                t_2 = result[j][2]
                result[j][0] = result[j+1][0]
                result[j][1] = result[j + 1][1]
                result[j][2] = result[j+1][2]
                result[j+1][0] = t_0
                result[j + 1][1] = t_1
                result[j+1][2] = t_2


    result = np.array(result)
    result = result.transpose()
    return result

# Testing
print(main([['0.22;Фачук М.К.', None, 'Не выполнено'],
            ['0.97;Нумузян Д.Д.', None, 'Выполнено'],
            ['0.06;Сетениди О.В.', None, 'Не выполнено']
            ]))


