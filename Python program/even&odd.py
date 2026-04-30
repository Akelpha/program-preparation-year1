"""Ecrire une fonction qui prend en argument un tuple et qui retourne le produit des nombres pairs et le
produit des nombres impaires."""

def even_odd(T):
    pEven = 1
    pOdd = 1
    for x in T:
        if x % 2 == 0:
            pEven *=x
        else:
            pOdd *=x
    
    return (pEven,pOdd)

t = (3, 17, 42, 8, 55, 91, 26, 74, 13, 60)
print(even_odd(t))
