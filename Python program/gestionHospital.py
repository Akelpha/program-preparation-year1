class Personne:

    def __init__(self, nom, age, cin):
        self.nom = nom
        self.age = age
        self.__cin = cin   # encapsulation


    # ===== Encapsulation =====

    def get_cin(self):
        return self.__cin

    def set_cin(self, cin):
        self.__cin = cin


    # ===== Méthode d'instance =====

    def afficher_infos(self):
        print(f"Nom : {self.nom}")
        print(f"Age : {self.age}")
        print(f"CIN : {self.__cin}")


    # ===== Méthode statique =====

    @staticmethod
    def est_majeur(age):
        return age >= 18


    # ===== Méthode de classe =====

    @classmethod
    def personne_anonyme(cls):
        return cls("Inconnu", 0, "XXXX")



# =====================================
# Héritage
# =====================================

class Patient(Personne):

    def __init__(self, nom, age, cin, maladie):
        super().__init__(nom, age, cin)
        self.maladie = maladie


    # polymorphisme
    def afficher_infos(self):
        super().afficher_infos()
        print(f"Maladie : {self.maladie}")



class Medecin(Personne):

    def __init__(self, nom, age, cin, specialite):
        super().__init__(nom, age, cin)
        self.specialite = specialite


    # polymorphisme
    def afficher_infos(self):
        super().afficher_infos()
        print(f"Specialite : {self.specialite}")



class Infirmier(Personne):

    def __init__(self, nom, age, cin, service):
        super().__init__(nom, age, cin)
        self.service = service


    # polymorphisme
    def afficher_infos(self):
        super().afficher_infos()
        print(f"Service : {self.service}")



# =====================================
# Classe Salle
# =====================================

class Salle:

    def __init__(self, numero, capacite):
        self.numero = numero
        self.capacite = capacite
        self.patients = []


    def ajouter_patient(self, patient):

        if len(self.patients) < self.capacite:
            self.patients.append(patient)
            print(f"{patient.nom} ajouté à la salle")
        else:
            print("Salle pleine")


    def afficher_patients(self):

        print(f"Patients dans la salle {self.numero} :")

        for patient in self.patients:
            print(patient.nom)



# =====================================
# Classe RendezVous
# =====================================

class RendezVous:

    def __init__(self, patient, medecin, date):
        self.patient = patient
        self.medecin = medecin
        self.date = date


    def afficher_rdv(self):

        print("===== Rendez-vous =====")
        print(f"Patient : {self.patient.nom}")
        print(f"Médecin : {self.medecin.nom}")
        print(f"Date : {self.date}")



# =====================================
# Programme principal
# =====================================

p1 = Patient("Amine", 20, "AA11", "Grippe")
p2 = Patient("Yassine", 30, "CC33", "Fièvre")

m1 = Medecin("Sara", 45, "BB22", "Cardiologie")

i1 = Infirmier("Lina", 28, "DD44", "Urgences")


# polymorphisme
p1.afficher_infos()

print()

m1.afficher_infos()

print()

i1.afficher_infos()


print()

# méthode statique
print(Personne.est_majeur(20))


print()

# méthode de classe
p3 = Personne.personne_anonyme()
p3.afficher_infos()


print()

# salle
salle1 = Salle(101, 2)

salle1.ajouter_patient(p1)
salle1.ajouter_patient(p2)

salle1.afficher_patients()


print()

# rendez-vous
rdv1 = RendezVous(p1, m1, "12/06/2026")

rdv1.afficher_rdv()