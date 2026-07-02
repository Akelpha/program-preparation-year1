class Etudiant:
    def __init__(self, name, prenom):
        self.name= name
        self.prenom = prenom
        self.notes =[]
    def moyenne(self):
        return sum(self.notes)/len(self.notes)
    

