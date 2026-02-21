"""Écrire un programme en langage Python qui affiche tous les diviseurs d’un entier positif n non nul."""
n = int(input("Enter a number"))
while n==0:
    n= int(input("Enter a number different to zero"))
    if n!=0:
        break

for i in range(1,n+1,1):
    if n % i == 0:
        print(i)
