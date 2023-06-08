def main(arr):
    m =[[1999, 'BOO', 1969, 0],
        [1999, 'BOO', 1986, 1],
        [1999, 'BOO', 2000, 2],
        [1999, 'NIX', 1992, 3],
        [1999, 'NIX', 1987, 4],
        [1999, 'NIX', 1986, 5],
        [1985, 'BOO', 1969, 6],
        [1985, 'BOO', 1986, 7],
        [1985, 'BOO', 2000, 8],
        [1985, 'NIX', 1992, 9],
        [1985, 'NIX', 1987, 10],
        [1985, 'NIX', 1986, 11]]

    for j in m:
        if arr[0] == j[0]:
            if arr[1] == j[1] and arr[1] == 'BOO':
                if arr[2] == j[2]:
                    return j[3]
            elif arr[1] == j[1] and arr[1] == 'NIX':
                if arr[3] == j[2]:
                    return j[3]


print(main([1999, 'NIX', 2000, 1992]))
print(main([1985, 'NIX', 1986, 1987]))
print(main([1985, 'BOO', 2000, 1986]))
print(main([1985, 'BOO', 1969, 1992]))
print(main([1985, 'NIX', 1986, 1986]))