print('x y z w')

for x in range(2):
   for y in range(2):
       for z in range(2):
           for w in range(2):
               if( (not(x) and not(y)) or (y == z) or not(w) ) == False:
                   print(x,y,z,w)

## bank-ege.ru id: 1673 ##