from itertools import *
k = 0

for s in product("АЕКМНЬ", repeat = 6):
    k += 1
    if s[0] != 'Ь' and s.count('М') == 2 and s.count('А') <= 1:
        print(k)