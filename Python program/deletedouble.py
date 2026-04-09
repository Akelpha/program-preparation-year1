"""Écrire un programme Python qui permet de supprimer les éléments dupliqués d'une liste."""


def deleteDouble(L):
    L1 = []
    for x in L:
        if x not in L1:
            L1.append(x)
    return L1

L = [4,4,8,4,9,7,7]
print(deleteDouble(L))