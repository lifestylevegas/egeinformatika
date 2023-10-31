res = set()
for n in range(1000):
    n2=bin(n)[2:]

    if n%3==0:
        n2=n2+n2[-3:]
    else:
        ost=n%3
        ost3=ost*3
        ost2=bin(ost3)[2:]
        n2=n2+ost2

    R = int(n2,2)
    if R>151:
        res.add(R)

print(min(res))
