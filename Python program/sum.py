"""Écrire un programme en Python qui demande à l'utilisateur de saisir un nombre entier n et de lui
afficher la valeur de la somme 1 + 2 + ... + n = ?"""
"""Écrire un programme qui calcule et affiche la somme de la série :
S= 1 + 10 + 100 + - + 10" """

s = 0
sSerie = 0
n = int(input("Enter a value. "))

for i in range(0,n+1,1):
    s +=i 
print(f"La somme est {s}")
for i in range(0,n+1,1):
    sSerie +=pow(10,i)
print(f"la somme de la serie est {sSerie}")