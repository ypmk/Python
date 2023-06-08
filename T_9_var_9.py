def main(args):
    result = []
    for i in args:
        row = []
        row.append(i[0] + '000')
        s = i[1]
        row.append(s[3:].replace(' ','').replace('-',''))
        s = i[2]
        row.append(s[4:]+' '+s[0:2])
        if row not in result:
            result.append(row)
    return result

print(main([['1.0','+7.txt 122 016-28-31','С.Ч. Чатегяк','С.Ч. Чатегяк'],
            ['0.3','+7.txt 017 630-52-38','Д.Д. Тоций','Д.Д. Тоций'],
            ['0.4','+7.txt 817 148-27-71','К.В. Тачли','К.В. Тачли'],
            ['0.4','+7.txt 817 148-27-71','К.В. Тачли','К.В. Тачли'],
      ]))

