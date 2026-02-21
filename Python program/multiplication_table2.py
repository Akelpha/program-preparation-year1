"""1) - Ecrire un programme en Python qui demande à l’utilisateur de saisir un nombre entier n et de lui afficher la table de multiplication de ce nombre.
2) - Améliorez le programme afin qu’il affiche les tables de multiplications de tous les nombres compris entre 1 et 7."""

 


# (1)

"""
n = int(input("Enter a number"))
for i in range(10):
    print(f"{n} * {i} = {n*i}" )"""
# (2)
for i in range(1,8,1):
    print(f"The multiplication table of {i}")
    for j in range(1,10,1):
        print(f"{j} * {i} = {j*i}" )

