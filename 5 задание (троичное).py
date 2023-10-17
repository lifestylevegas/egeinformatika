def f3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s
min1 = 9999
for i in range(1, 1000):
    n = f3(i)
    if i % 3 == 0:
        n += n[-2:]
    else:
        ost = i % 3 * 5
        n += f3(ost)
    r = int(n, 3)
    if r > 150:
        min1 = min(min1, r)
print(min1)

## bank-ege.ru id: 23738 ##
