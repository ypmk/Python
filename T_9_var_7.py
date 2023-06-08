import numpy as np


def main(args):
    result = []
    for i in args:
        row = []
        s = i[2]
        l = s[2:4]
        if int(s[4]) >= 5:
            l = s[2]+str(int(s[3])+1)
        row.append(l+'%')
        s = i[2].split(';')[1]
        m = s.split(',')[1]
        row.append(s.split(',')[0] + m[0:3])
        if i[3] == 'Да':
            row.append('Y')
        else:
            row.append('N')
        k = i[4].replace('-', '')
        s = k[4]+k[5]+'.'+k[2]+k[3]+'.'+k[0]+k[1]
        row.append(s)
        result.append(row)

    result = sorted(result, key=lambda a:a[1])
    result = np.array(result)
    result = result.transpose()

    return result



print(main([[None, None, '0.282;Вибифяк, Я.М.', 'Да', '03-10-02'],
            [None, None, '0.991;Вецубман, Ф.К.', 'Да', '00-01-18'],
            [None, None, '0.617;Китозий, М.Д.', 'Да', '03-06-07'],
            ]))













