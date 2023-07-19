def ss5(n):
    s = ''
    while n != 0:
        s = str(n % 5) + s
        n = n // 5
    return s

def summ(n):
    s = 0
    while n != 0:
        s = s + n % 10
        n = n // 10
    return s

k = 0
for n in range(1, 400 + 1):
    n5 = ss5(n)
    if n % 4 == 0:
        n5 = n5 + n5[:2]
    else:
        ost = n % 5
        ost7 = ost * 7
        ost5 = ss5(ost7)
        n5 = n5 + ost5
    r = int(n5, 5)
    s = summ(r)
    if s % 5 == 0:
        k += 1

print(k)