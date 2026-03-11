"""Écrire le script qui affiche en fonction d'une valeur saisie par l'utilisateur l'un des messages suivants :
"Ce nombre est pair"
"Ce nombre est impair, mais est multiple de 3"
"Ce nombre n'est ni paír ni multiple de 3" 
"""

a = int(input("Enter a value. "))

if a % 2 == 0:
    print(f"{a} est pair.")
elif a%2 !=0 and a % 3 == 0:
    print(f"{a} est impair, mais est multiple de 3")
else:
    print(f"{a} n'est ni pair ni multiple de 3.")