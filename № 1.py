for n in range(1, 200 + 1):
    n2 = bin(n)[2:]
    s = n2.count('1')
    if s % 2 == 0:
        n2 = n2 + '10'
    else:
        n2 = n2 + '01'
    r = int(n2, 2)
    if r % 2 == 0:
        res = n

print(res)
