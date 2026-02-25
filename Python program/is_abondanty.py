"""Écrire une fonction est_abondant avec un paramètre n (nombre entier). Cette fonction doit retourner 1 si l’entier n est abondant et 0 sinon.
(Un entier est dit Abondant : s’il est strictement inférieur à la somme de ses diviseurs propres.)
Tester la fonction par un appel dans le programme principal."""

def abondant (n):
    s = 0
    for i in range(1,n,1):
        if n % i == 0:
            s+=n
    if n < s:
        return 1
    else:
        return 0      

number = int(input("Enter a number: "))
print(abondant(number))