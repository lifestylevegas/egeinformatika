for n in range(1, 100):
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s += '0'
    else:
        s += '1'
    if s.count('1') % 2 == 0:
        s += '0'
    else:
        s += '1'
    r = int(s, 2)
    if r > 93:
        print(r)
        break
