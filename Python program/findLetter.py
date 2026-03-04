"""Ecrire un programme en Python qui demande à l’utilisateur de saisir une chaine de caractère S et de lui renvoyer un message indiquant si la chaine contient la lettre 'a' tout en indiquant sa position sur la chaine. Exemple si l’utilisateur tape la chaine s = ‘langage’ le programme lui renvoie : La lettre 'a' se trouve à la position : 1 La lettre 'a' se trouve à la position : 4""" 

# Essaie numero 1
# S = input("Enter a string: ")
# sPosition=S.rfind("a")
# print(f"La lettre 'a' se trouve à la position : {sPosition}")

# Find letter a with for loop
"""phrase = input("Enter a phrase: ")
for i in range(len(phrase)):
    if phrase[i] == 'a':
        print(f"La lettre 'a' se trouve à la position : {i}")"""


# Find a letter  with for loop

phrase = input("Enter a phrase: ")
c = input("Enter the letter that you want to search.")

for i in range(len(phrase)):
     if phrase[i] == c:
        print(f"La lettre {c} se trouve à la position : {i}")

# Find a letter with a string method
"""phrase = input("Enter a phrase: ")
c = input("Enter the letter that you want to search.")

print(phrase.count(c))
"""