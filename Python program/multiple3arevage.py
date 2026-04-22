"""Ecrire une fonction moyenne qui prend en argument une liste de nombres et renvoie la
moyenne des nombres multiples de 3 présents dans la liste."""

def moyenne(liste):
    s = 0
    count = 0
    for x in liste:
        if x % 3 == 0:
            count +=1
            s += x
    moyenne = s/count
    return moyenne
L=[]
n= int(input("Entrer the length of the list: "))
for i in range(n):
    x= int(input("Enter a interger: "))
    L.append(x)

print(moyenne(L))