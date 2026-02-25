"""Ecrire un programme en Python qui demande à l’utilisateur de saisir une chaine de caractère S et de lui renvoyer un message indiquant si la chaine contient la lettre 'a' tout en indiquant sa position sur la chaine. Exemple si l’utilisateur tape la chaine s = ‘langage’ le programme lui renvoie : La lettre 'a' se trouve à la position : 1 La lettre 'a' se trouve à la position : 4""" 


S = input("Enter a string: ")
sPosition=S.rfind("a")
print(f"La lettre 'a' se trouve à la position : {sPosition}")