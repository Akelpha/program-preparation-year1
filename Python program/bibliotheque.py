class Personne:
    def __init__(self,nom,prenom,age):
        self.nom = nom 
        self.prenom = prenom 
        self.__age = age 
    def get_age(self):
        return self.__age
    def set_age(self,newage):
        self.__age = newage
        return self.__age
    def afficher_personne(self):
        print(f"Nom : {self.nom}")
        print(f"Prénom : {self.prenom}")
        print(f"Âge : {self.__age}")
class Membre(Personne):
    def __init__(self,nom,prenom,age,num_member):
        super().__init__(nom,prenom,age)
        self.num_member = num_member
        self.livres_emprutes = []
    def emprunter_livres(self,livre,bibliotheque,bibliothecaire):
        if livre in bibliotheque and livre not in self.livres_emprutes :
            self.livres_emprutes.append(livre)
            bibliothecaire.supprimer_livre(livre,bibliotheque)
    def rendre_livre(self,livre,bibliotheque,bibliothecaire):
        if livre in self.livres_emprutes and livre not in bibliotheque:
            self.livres_emprutes.remove(livre)
            bibliothecaire.ajouter_livre(livre,bibliotheque)
class Livre:
    def __init__(self,titre,auteur,annee_publication):
        self.auteur = auteur
        self.titre = titre
        self.annee_publication = annee_publication

    def afficher_details(self):
       print(f"Titre : {self.titre}")
       print(f"Auteur : {self.auteur}")
       print(f"Année de publication : {self.annee_publication}")

    def __str__(self):
        return f"{self.titre} - {self.auteur} ({self.annee_publication})"

class bibliothecaire(Personne):
    def __init__(self,nom,prenom,age,num_employe,role):
        super().__init__(nom,prenom,age)
        self.__num_employe = num_employe
        self.role = role
    
    def get_num_employe(self):
        return self.__num_employe
    def set_num_employe(self,new_num_employe):
        self.__num_employe = new_num_employe




