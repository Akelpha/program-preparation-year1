# =====================================
# Classe Produit
# =====================================

class Produit:

    def __init__(self, nom, annee_fabrication, prix):

        self.nom = nom
        self.annee_fabrication = annee_fabrication
        self.__prix = prix     # attribut privé


    # ===== Encapsulation =====

    def get_prix(self):
        return self.__prix


    def set_prix(self, prix):

        if prix > 0:
            self.__prix = prix
        else:
            print("Prix invalide")


    # ===== Affichage =====

    def Afficher(self):

        print("===== Produit =====")
        print(f"Nom : {self.nom}")
        print(f"Année : {self.annee_fabrication}")
        print(f"Prix : {self.__prix}")


    # ===== Calcul prix =====

    def CalculPrix(self):

        

        anciennete = 2026 - self.annee_fabrication

        prix_final = self.__prix

        if anciennete < 10:
            prix_final = self.__prix * 0.95

        return prix_final



# =====================================
# Classe ProduitElectronique
# =====================================

class ProduitElectronique(Produit):

    def __init__(self, nom, annee_fabrication, prix,
                 garantie, consommation):

        super().__init__(nom, annee_fabrication, prix)

        self.garantie = garantie
        self.consommation = consommation


    # polymorphisme
    def Afficher(self):

        super().Afficher()

        print(f"Garantie : {self.garantie}")
        print(f"Consommation : {self.consommation} W")


    # polymorphisme
    def CalculPrix(self):

        prix_final = self.get_prix()

        if self.consommation < 500:
            prix_final = prix_final * 0.90

        return prix_final



# =====================================
# Classe ProduitAlimentaire
# =====================================

class ProduitAlimentaire(Produit):

    def __init__(self, nom, annee_fabrication, prix,
                 date_expiration, poids):

        super().__init__(nom, annee_fabrication, prix)

        self.date_expiration = date_expiration
        self.poids = poids


    # polymorphisme
    def Afficher(self):

        super().Afficher()

        print(f"Date expiration : {self.date_expiration}")
        print(f"Poids : {self.poids} kg")


    # polymorphisme
    def CalculPrix(self):

        prix_final = self.get_prix()

        if self.poids > 5:
            prix_final = prix_final * 0.85

        return prix_final



# =====================================
# Programme principal
# =====================================

p1 = Produit("Chaise", 2020, 1000)

e1 = ProduitElectronique(
    "Télévision",
    2022,
    5000,
    "2 ans",
    300
)

a1 = ProduitAlimentaire(
    "Riz",
    2024,
    200,
    "12/12/2026",
    10
)


# ===== Affichage =====

p1.Afficher()
print("Prix après réduction :", p1.CalculPrix())

print()

e1.Afficher()
print("Prix après réduction :", e1.CalculPrix())

print()

a1.Afficher()
print("Prix après réduction :", a1.CalculPrix())