k=0
for x1 in '1234567':
    for x2 in '01234567':
        for x3 in '01234567':
            for x4 in '01234567':
                for x5 in '01234567':
                    s = x1+x2+x3+x4+x5
                    if s.count('1')==0:
                        if s.count(x1)==1 and s.count(x2)==1 and s.count(x3)==1 and s.count(x4)==1 and s.count(x5)==1:
                            if x1 in '1357' and x2 in '0246' and x3 in '1357' and x4 in '0246' and x5 in '1357':
                                k+=1
                            if x1 in '246' and x2 in '1357' and x3 in '0246' and x4 in '1357' and x5 in '0246':
                                k+=1
print(k)

