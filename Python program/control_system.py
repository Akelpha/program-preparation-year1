"""🧠 Exercice : Mini système de contrôle d’accès
Tu dois écrire un programme qui :
Demande à l’utilisateur :
son nom
son âge
le nombre de tentatives 
Le programme doit :
Refuser l’accès si l’âge est < 18
Refuser l’accès si le nombre de tentatives ≥ 3
Sinon autoriser l’accès
Le programme doit continuer à demander les informations
tant que l’accès est refusé,
sauf si le nombre de tentatives atteint 3."""

name = input("What is your name ?")
age = int(input("What is your age?"))
tentative = 0

while tentative < 3 :
    name = input("What is your name ?")
    age = int(input("What is your age?"))
    if(age < 18):
        print("Access denied")
        tentative +=1
    break
if(tentative>=3):
    print("Tentative number reached!!")
