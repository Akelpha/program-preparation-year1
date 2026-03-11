# L’ordinateur choisit un nombre secret entre 1 et 50.
# L’utilisateur doit deviner.
# Le programme doit :
# répéter jusqu’à ce que le joueur trouve
# dire si le nombre est trop grand ou trop petit
# compter le nombre de tentatives
# afficher un message spécial selon la performance
# plus petit → afficher “Trop petit”

# plus grand → afficher “Trop grand”

# égal → afficher “Bravo” + sortir de la boucle
# Ce que tu vas utiliser

# TODO : utiliser la bibliothèque random pour générer le nombre secret aléatoire quand je comprendrai mieux

secret_number= 94;
tentative =0;
while True:
    user_number = int(input("Can you guess the number: "))
    tentative +=1
    if user_number <secret_number:
        print("Too small")
        
    elif user_number>secret_number:
        print("Too big")

    else:
        print("You guess the number!!")
        break
    
if tentative <=5:
    print("You guess this number quickly")
elif 6 <= tentative <= 10:
    print("You could guess it faster😔!")
else :
    print("You could have done better!")


