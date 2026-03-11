""""Écrire un programme qui demande à l’utilisateur de saisir un nombre entier n et de vérifier si le nombre est parfait ou non."""

"""
while n==0:
    n= int(input("Enter a number different to zero"))
    if n!=0:
        break

for i in range(1,n+1,1):
    if n % i == 0:
        print(i)"""
def perfect(n):
    s = 0
    for i in range(1,n,1):
        if n % i == 0:
            s +=i

    if n == s:
        print(f"{n} is a perfect number")
    else:
        print(f"{n} isn't a perfect number")


n = int(input("Enter a number"))
perfect(n)

