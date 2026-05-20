class Personne :
    def __init__(self,nom,prenom,age):
        self.nom = nom
        self.prenom = prenom 
        self.age = age

    def Afficher_infos(self):
        print("Les Informations de la personne")
        print(f"Nom : {self.nom}")
        print(f"Prenom: {self.prenom}")
        print(f"Age: {self.age}")
    def Anniversaire(self):
        self.age +=1
        return self.age
    
class Etudiant(Personne):
    def __init__(self,nom,age,prenom,liste_etudiants):
        super().__init__(nom,age,prenom)
        self.liste_etudiants = liste_etudiants

    def Anniversaire(self):
        super().anniversaire()
        return f"Bonjour {self.prenom} votre age {self.age}"
    def afficher_etudiant(self):
        