from itertools import *

def f(x):
    P = 25<=x<=50
    Q = 54<=x<=75
    A = a1<=x<=a2
    return Q <= ((P == Q)or((not P)<=A))

ox = [i/4 for i in range(24*4,76*4)]
m = []

for a1,a2 in combinations(ox,2):
    if all(f(x)==1 for x in ox):
        m.append(a2-a1)

print(min(m))
