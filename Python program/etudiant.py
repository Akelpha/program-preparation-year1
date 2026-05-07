class Etudiant:

    def __init__(self,nom,prenom,notes):
        self.nom = nom
        self.prenom = prenom
        self.notes = notes

    def moyenne(self):
        if len(self.notes) == 0:
            return 0
        return sum(self.notes)/len(self.notes)
    def Afficher_infos(self):
        print("Nom : ", self.nom)
        print("Prenom : ", self.prenom)
        print("Moyenne :",self.moyenne())


etudiant1 = Etudiant("Dupont", "Marie", [14, 16, 12, 18, 15])
etudiant1.Afficher_infos()