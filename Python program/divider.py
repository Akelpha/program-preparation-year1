"""Écrire un programme en langage Python qui affiche tous les diviseurs d’un entier positif n non nul."""

def diviseur(n):
    for i in range(1,n+1,1):
        if n % i == 0:
            print(i)
n = int(input("Enter a number"))
while n<=0:
    n= int(input("Enter a number above zero"))
    if n >0:
        break

diviseur(n)