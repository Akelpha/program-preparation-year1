"""Écrire une fonction triangulaire avec un paramètre n (nombre entier). Cette fonction doit retourner 1 si l’entier n est triangulaire et 0 sinon. Tester la fonction par un appel dans le programme principal.
Un nombre n est dit triangulaire s’il existe un k > 0 tel que : n=1+2+…+k
Exemple : 15 est un nombre triangulaire car 15=1+2+3+4+5"""

 

def triangulaire(n):
    s = 0
    k= 0
    while s < n:
        s +=k
        k+=1
    if s == n:
        return 1
    else: 
        return 0



n = int(input("Enter a number"))
if triangulaire(n):
    print(f"{n} est un nombre triangulaire ")
else:
    print(f"{n} n'est pas un nombre triangulaire ")