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
        print("Date De Naissancec: ",self.DateNaissance.ToString())

class Employe(Personne):
    def __init__(self,nom,prenom,DateNaissance,salaire):
        super().__init__(nom,prenom,DateNaissance)
        self.salaire = salaire
    
    def afficher(self):
        super().afficher()
        print(self.salaire)


class chef(Employe):
    def __init__(self,nom,prenom,DateNaissance,salaire,nom_Service):
        super().__init__(nom,prenom,DateNaissance,salaire)
        self.nom_Service = nom_Service
    def afficher(self):
        super().afficher()
        print(self.nom_Service)



# Création des dates de naissance
date1 = DateNaissance(15, 3, 1990)
date2 = DateNaissance(22, 7, 1985)
date3 = DateNaissance(10, 8, 2000)

# Création d'une Personne
personne1 = Personne("Alaoui", "Fatima", date1)

print("---")

# Création d'un Employé
employe1 = Employe("Benjelloun","Youssef",date2,5000)

print("---")

# Création d'un Chef
chef1 = chef("Talibi", "Mohamed", date3,1500,"Informatique")



L1=[personne1,employe1,chef1]
for i in L1:
    i.afficher()  

        