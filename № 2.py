for n in range(100):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 = n2.replace('1', '11')
    else:
        n2 = n2.replace('0', '00')
    r = int(n2, 2)
    if r > 170:
        print(n, r)
        break
