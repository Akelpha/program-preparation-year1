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


L = []
n = int(input("Enter the list length: "))
for i in range(n):
    x = int(input("Enter the element: "))
    L.append(x)
print(inf_moy(L))