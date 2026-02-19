"""Écrire un programme qui demande à l'utilisateur de saisir deux valeurs numériques. Si les deux
valeurs sont divisibles par 5, le programme échange leurs contenus. Sinon, il affecte à la première
valeur la somme des deux, et à la seconde leur produit. Enfin, le programme affiche les nouvelles
valeurs des deux données."""

x = int(input("Enter a value 1."))
y = int(input("Enter a value 2."))
s =x+y
p = x*y
new_x = x
new_y = y
if x and y % 5 ==0:
    new_x = y
    new_y = x
else:
    new_x = s
    new_y = p


print(f"les nouvelles valuers de deux données sont {new_x} et {new_y}")

