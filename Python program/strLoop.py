"""Ecrire un programme en langage Python qui permet de parcourir et afficher les caractères d’une variable du type chaine de caractères. Exemple pour s = « Python », le programme affiche les caractères :
P
y
t
h
o
n"""

c = input("Enter a string: ")
# 1ere methode
for x in c :
    print(x)
# 2eme methode
for i in range(len(c)):
    print(c[i])