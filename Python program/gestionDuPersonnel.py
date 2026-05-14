class DateNaissance:
    def __init__(self,jour,mois,annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee
    def ToString(self):
        return f"{self.jour}/{self.mois}/{self.annee}"
        # return str(self.jour)+" / "+str(self.mois)+ " / "+str(self.annee)
    
class Personne:
    def __init__(self,nom,prenom,DateNaissance):
        self.nom = nom 
        self.prenom = prenom 
        self.DateNaissance = DateNaissance
    def afficher(self):
        print("Les Informations De la personne")
        print("Nom: ",self.nom)
        print("Prenom: ",self.prenom)
        print("Date De Naissancec: ",self.DateNaissance)

class Employe(Personne):
    def 

        
        