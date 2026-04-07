

def sumOfList(L):
    s=0
    for x in L:
        if type(x) == int:
            s += x
        elif type(x) == list:
            s +=sum(x)
    return s

liste =[1,2,[3,4,5,6],71,8,[9]]

print(sumOfList(liste))
