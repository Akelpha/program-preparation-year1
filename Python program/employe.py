class Employe:
    def __init__(self,Matricule, Nom, Prenom, AnneeNaissance, AnneeEmbauche, Salaire):
        self.Matricule = Matricule
        self.Nom = Nom
        self.Prenom = Prenom 
        self.AnneeNaissance = AnneeNaissance
        self.AnneeEmbauche = AnneeEmbauche
        self.Salaire = Salaire
    
    def age(self):
        return 2026-self.AnneeNaissance
    def anciennete(self):
        return 2026-self.AnneeEmbauche
    def augmenter_salaire(self):
        if self.anciennete() < 5 :
            self.Salaire *= 1.02
        elif self.anciennete() < 10 :
            self.Salaire *= 1.05
        else:
            self.Salaire *= 1.10
    def afficher_employe(self):
        print("- Matricule    :", self.Matricule)
        print("- Nom complet  :", self.Nom, self.Prenom)
        print("- Age          :", self.age())
        print("- Ancienneté   :", self.anciennete(), "ans")
        print("- Salaire      :", self.Salaire, "DH")
        print()



emp1 = Employe("E001", "Alami", "Youssef", 28, 3, 5000)   # < 5 ans → +2%
emp2 = Employe("E002", "Benali", "Sara", 35, 7, 8000)     # < 10 ans → +5%
emp3 = Employe("E003", "Chraibi", "Omar", 45, 15, 12000)  # >= 10 ans → +10%

emp1.augmenter_salaire()
emp1.afficher_employe() 
emp2.augmenter_salaire()
emp2.afficher_employe()
emp3.augmenter_salaire()
emp3.afficher_employe()