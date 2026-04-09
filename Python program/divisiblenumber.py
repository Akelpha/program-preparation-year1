"""Créez une fonction Python, appelée nombreDivisible, qui s'applique à une liste de nombres
L = [12 , 04 , 14 , 11 , 18 , 13 , 07, 10 , 05 , 09 , 15 , 08 , 14 , 16] et un entier n entré par
l’utilisateur, et qui renvoie le nombre d’éléments de la liste qui sont divisible par n ."""


def nombreDivisible(L):
    count = 0
    n = int(input("Enter a integer: "))
    for i in range(len(L)):
        if L[i] % n == 0:
            count +=1
    return count

    
    

L = [12 , 4 , 14 , 11 , 18 , 13 , 7, 10 , 5 , 9 , 15 , 8 , 14 , 16]
print(nombreDivisible(L))