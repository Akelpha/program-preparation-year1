"""Ecrire un programme python qui demande a l'utilisateur de saisr un nombre entier n et de lui afficher si ce nombre est premier ou non"""

def premier(n):
    for i in range(2,n,1):
        if n % i==0:
            print(f"{n} n'est pas premier")
            break
    else:
        print(f"{n} est premier")
              

        
n= int(input("Enter a number: "))
premier(n)




