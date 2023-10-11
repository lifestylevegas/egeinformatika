from itertools import *
k = 0 

for x in product("ЗИКЛМН",repeat=4):
    s = ''.join(x)
    if s.count("З")==1:
        k+=1
print(k)

## bank-ege.ru id: 820 ##
