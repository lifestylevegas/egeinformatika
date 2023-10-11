print('x y z w')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if( z and not(x) and (not(w) or y) ) == True:
                    print(x,y,z,w)

## bank-ege.ru id: 1822 ##