"""Exercice 2 """

class Voiture:
    def __init__(self,marque,modele,annee,vitesse,couleur,kilometrage,moteur):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.vitesse =vitesse
        self.couleur =couleur
        self.kilometrage = kilometrage
        self.moteur = moteur
    def accelerer(self):
        self.vitesse +=10
    def afficher_vitesse(self):
        print(self.vitesse)
    def est_ancienne(self):
        if 2026-self.annee > 10:
            return True
        else:
            return False
    def changer_couleur(self,newColor):
        self.couleur = newColor
        print(self.couleur)
    def est_usee(self):
        if self.kilometrage > 100000:
            return True
        else:
            return False
        

voiture1 = Voiture("Toyota","TX",2017,70,"rouge",10000,"Diesel")
voiture1.accelerer()
voiture1.afficher_vitesse()
print(voiture1.est_ancienne())
voiture1.changer_couleur("orange")
print(voiture1.est_usee())