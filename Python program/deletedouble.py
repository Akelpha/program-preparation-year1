"""Écrire un programme Python qui permet de supprimer les éléments dupliqués d'une liste."""


def deleteDouble(L):
    for x in L:
        while L.count(x) > 1:
            L.remove(x)
        # if x not in L1:
        #     L1.append(x)
    return L

L = [4,4,8,8,6,6,10,19,4,9,7,7]
print(deleteDouble(L))