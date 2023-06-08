def main(*r):
    s = (
        {'', '', ''},
        {'', '', ''})
    s1 = set(*r)
    return [i for i in range(len(s))
            if not(len(s[i] - s1))][0]


print(main(['', '', ''))