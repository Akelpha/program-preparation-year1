"""Écrire une fonction « premier » qui affiche tous les nombres premiers entre limite inférieure et limite supérieure les deux limites sont deux paramètres saisis par l’utilisateur."""

"""n = int(input("Enter a value. "))

if n % (n and 1) == 0:
    print(f"{n} est un nombre premier. ")
else :
    print(f"{n} n'est pas un nombre premier.")
"""

def premier (limInf,limSup):
    for i in range(limInf,limSup+1,1):
        if i %(i and 1) == 0:
            print(i)
        

limInfe = int(input("Enter a number as a inf limit")) 
limSupe = int(input("Enter a number as a Sup limit"))

premier(limInfe,limSupe)