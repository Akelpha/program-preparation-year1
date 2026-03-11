"""Écrire une fonction « premier » qui affiche tous les nombres premiers entre limite inférieure et limite supérieure les deux limites sont deux paramètres saisis par l’utilisateur."""



def premier (limInf,limSup):
    for i in range(limInf,limSup+1):
        if i < 2:
            continue
        for j in range(2,i):
            if i%j == 0:
               break
        else:
                print(i)
        

limInfe = int(input("Enter a number as a inf limit: ")) 
limSupe = int(input("Enter a number as a Sup limit: "))

premier(limInfe,limSupe)  