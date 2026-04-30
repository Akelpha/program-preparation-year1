"""Écrire une fonction python qui attend une liste imbriquée d’entiers et retourne la somme de tous les
entiers pairs qu’elle contient.
Par exemple pour cette liste : L= [[1, 2, 3], [4, 5], [6, 8, 9, 7]] doit retourner 20."""

def sumOfeven(L):
    s=0
    for x in L:
        for y in x:
            if y % 2 == 0:
                s+=y
    return s


L= [[1, 2, 3], [4, 5], [6, 8, 9, 7]] 

print(sumOfeven(L))