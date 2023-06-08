def main(x):
    x = x.replace('begin', '')\
        .replace('<<', '')\
        .replace('local', '')\
        .replace('>>', '')\
        .replace('\'', '')\
        .replace('\n', '')\
        .replace(' ', '')\
        .replace('#', '')
    print(x)
    x_parts = x.split('end')
    x_parts.pop(-1)
    x_parts1 = [i.split('::=') for i in x_parts]
    result = []
    for i in range(len(x_parts1)):
        value = int(x_parts1[i][1])
        key = x_parts1[i][0]
        result.append((key, value))
    return result


# Testing
print(main('<<begin local inbia ::= #-7934 end begin local xedibe_95 ::=#5519 end\nbegin local bicein::=#-9011 end begin local ceedes ::= #-2730 end >>'))

