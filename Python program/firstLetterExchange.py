"""Ecrire un programme en langage Python, permettant d’échanger le premier et le dernier caractère d’une chaine donnée."""


c = input("Enter a string: ")
print(f"{c[-1]}{c[1:len(c)-1]}{c[0]}")