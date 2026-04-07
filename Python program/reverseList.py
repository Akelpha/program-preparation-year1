L = list((19,51,6,[6,1,5],[8,6,5],12,[10,1,1]))
Lreverse = []
for x in L[::-1]:
    if type(x) == list:
        x.reverse()
        Lreverse.append(x)
    else:
        Lreverse.append(x)

print(Lreverse)