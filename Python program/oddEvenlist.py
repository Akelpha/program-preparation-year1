"""Écrire un programme Python qui permet d’extraire la liste des entiers pairs et la liste des
entiers impairs d’une liste de nombres."""

def oddEven(liste):
    listEven = []
    listOdd = []
    for i in range(len(liste)):
        if i % 2 == 0:
            listEven.append(i)
        elif i % 2 != 0:
            listOdd.append(i)
    print(listEven)
    print(listOdd)

liste = [1,2,3,4,5,6,7,8,9,10,11,12,141,15,16,18,19,20,24,25,256,43]
oddEven(liste)