"""Écrire une fonction table_multiplication avec trois paramètres : mul(multiplicateur), bornInf et bornSup.
Cette fonction doit afficher la table de multiplication avec les trois paramètres. Tester la fonction par un appel dans le programme principal."""
'''Par exemple : si mul =3 et bornInf = 2 et bornSup = 5, on aura comme résultat :
3*2=6
3*3=9
3*4=12
3*5=15'''


def multiplication(mul,bornInf,bornSup):
    for i  in range(bornInf,bornSup+1,1):
        print(f"{mul} * {i} = {mul*i}")

mul = int(input(("Enter a number")))
bornInf = int(input("Enter the begin of the multiplication table. "))
bornSup = int(input("Enter the begin of the multiplication table. "))

multiplication(mul,bornInf,bornSup)
    


