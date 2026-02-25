"""Ecrire un programme python qui demande a l'utilisateur de saisr un nombre entier n et de lui afficher si ce nombre est premier ou non"""

n = int(input("Enter a value. "))
# if n == 1 or 0:
#     print(f"{n} n'est pas un nombre premier. ")
if n % n and n % 1 == 0:
    print(f"{n} est un nombre premier. ")  

else :
    print(f"{n} n'est pas un nombre premier.")

