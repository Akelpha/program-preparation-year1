"""Écrire une fonction « premier » qui affiche tous les nombres premiers entre limite inférieure et limite supérieure les deux limites sont deux paramètres saisis par l’utilisateur."""


# TODO: Arranger cette fonction
def premier (limInf,limSup):
    for i in range(limInf,limSup+1,1):
        if i < 2:
            continue
        
        if i % i and i % 1 == 0:
            print(i)
        

limInfe = int(input("Enter a number as a inf limit: ")) 
limSupe = int(input("Enter a number as a Sup limit: "))

premier(limInfe,limSupe)  