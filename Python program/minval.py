# Ecrire un programmme qui demande a l'utilisateur de saisir 3 valeurs et qui affiche la plus petite des 3 valeurs.

a = int(input("Enter a value 1."))
b= int(input("Enter a value 2."))
c= int(input("Enter a value 3."))

if a > b and c > b:
    print(f"Le plus petit de 3 valeurs est {b}")
elif b > c:
    print(f"Le plus petit de 3 valeurs est {c}")
else:
    print(f"Le plus petit de 3 valeurs est {a}")
