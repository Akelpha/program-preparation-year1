class Vehicule:
    def __init__(self, marque, modele,annee,vitesse_max):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.vitesse_max = vitesse_max

    def afficher_infos(self):
        print(self.marque,self.modele,self.annee,self.vitesse_max)

class Voiture(Vehicule):
    def __init__(self, marque, modele,annee,vitesse_max,nombre_de_places):
        super().__init__(marque,modele,annee,vitesse_max)
        self.nombre_de_places = nombre_de_places
    def afficher_infos(self):
        super().afficher_infos()
        print(self.nombre_de_places)
class Moto(Vehicule):
    def __init__(self, marque, modele, annee, vitesse_max,type_de_moto):
        super().__init__(marque, modele, annee, vitesse_max)
        self.type_de_moto =type_de_moto
    def afficher_infos(self):
        super().afficher_infos()
        print(self.type_de_moto)
veh1 = Vehicule("Peugeot", "208", 2021, 190)
veh2 = Vehicule("Ford", "Focus", 2019, 210)
veh3 = Vehicule("Nissan", "Micra", 2018, 160)
v1 = Voiture("Toyota", "Corolla", 2020, 180, 5)
v2 = Voiture("BMW", "X5", 2022, 240, 7)
v3 = Voiture("Renault", "Clio", 2019, 170, 5)
m1 = Moto("Yamaha", "R1", 2021, 299, "Sportive")
m2 = Moto("Honda", "CB500", 2020, 190, "Roadster")
m3 = Moto("Harley-Davidson", "Iron 883", 2018, 170, "Custom")
veh1.afficher_infos()
veh2.afficher_infos()
veh3.afficher_infos()
v1.afficher_infos()
v2.afficher_infos()
v3.afficher_infos()
m1.afficher_infos()
m2.afficher_infos()
m3.afficher_infos()