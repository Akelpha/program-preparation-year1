"""Écrire une fonction inf_moy qui prend en argument une liste de nombres et qui affiche une
liste qui contient tous les nombres inférieurs à la moyenne des nombres impairs."""


def inf_moy(liste):
    s = 0
    count = 0
    listMoy = []
    for x in liste:
        if x % 2 != 0:
            count += 1
            s +=x
    moyenne = s/count
    for x in liste:
        if x < moyenne:
            listMoy.append(x)

    return listMoy


L = [3, 8, 11, 14, 5, 20, 7, 2, 9, 16, 1, 18, 13, 6, 15, 4, 19, 10, 17, 12]
print(inf_moy(L))