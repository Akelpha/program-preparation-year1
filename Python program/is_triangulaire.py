"""Écrire une fonction triangulaire avec un paramètre n (nombre entier). Cette fonction doit retourner 1 si l’entier n est triangulaire et 0 sinon. Tester la fonction par un appel dans le programme principal.
Un nombre n est dit triangulaire s’il existe un k > 0 tel que : n=1+2+…+k
Exemple : 15 est un nombre triangulaire car 15=1+2+3+4+5"""

 
# TODO: je dois arranger ca aussi , faire encore sorte que ca gere les nombre triangulaire
def triangulaire(n):
    t = (n**2+n)/2
    if n == t:
        return 1
    else: 
        return 0




n = int(input("Enter a number"))
print(triangulaire(n))