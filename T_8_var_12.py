def main(x):
    x = x.replace('<<', '')
    x = x.replace('|', '')
    x = x.replace('equ ', '')
    x = x.replace(' ', '')
    x = x.replace('>>', '')
    x = x.replace('<<', '')
    x_parts = x.split('.')
    x_parts.pop(-1)
    result = []
    for i in x_parts:
        key = i.split('q(')[0]
        value = i.split('q(')[1]
        result.append({key: value})
    return result


print(main('| << equ reis_225 q(arla_369)>>.<<equ anedbe q(quza_852) >>. |'))
#{'reis_225': 'arla_369', 'anedbe': 'quza_852'}