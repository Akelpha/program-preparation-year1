"""Écrire un programme Python qui permet d’extraire la liste des entiers pairs et la liste des
entiers impairs d’une liste de nombres."""

def oddEven(liste):
    listEven = []
    listOdd = []
    for i in range(len(liste)):
        if L[i] % 2 == 0:
            listEven.append(liste[i])
        elif L[i] % 2 != 0:
            listOdd.append(liste[i])
    print(listEven)
    print(listOdd)
L = []
n = int(input("Enter the list length: "))
for i in range(n):
    x = int(input("Enter the element: "))
    L.append(x)
oddEven(L)