class CompteBancaire:
    def __init__(self,numeroCompte,nom,solde):
        self.numeroCompte = numeroCompte
        self.nom = nom
        self.solde = solde

    def versement(self,amount):
        self.solde += amount
        print("le nouveau solde est: ",self.solde)
    def retrait(self,amount):
        if amount < self.solde:
            self.solde -= amount
        else:
            print("le solde insuffisant.")
    def afficher(self):
        print(f"le numero est :{self.numeroCompte}")
        print(f"le numero est :{self.nom}")
        print(f"le numero est :{self.solde}")

compt1 = CompteBancaire(123123,"Ali",2000)
compt1.versement(1000)
compt1.retrait(500)
compt1.afficher()