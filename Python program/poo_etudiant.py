class Etudiant:
    listE = []
    
    def __init__(self,nom,age,notes):
        self.nom=nom
        self.age=age
        self.notes= notes
        Etudiant.listE.append(self)
    
    @classmethod
    def afficher_tous(cls):
        for x in cls.listE:
            print(x.nom,x.age,x.notes)
    @classmethod
    def nombre_etudiants(cls):
        print(len(cls.listE))
    @classmethod
    def meilleur_notes(cls):
        meilleur = max(cls.listE, key=lambda x: sum(x.notes) / len(x.notes))
        print(meilleur.nom,meilleur.notes)

    @classmethod
    def moyenne(cls):
        s = 0
        for x in cls.listE:
            s+=sum(x.notes)
            # s = sum([e.note for e in cls.listE])
        return s/len(cls.listE)
    

etudiant1 = Etudiant("Dupont", 20, [14, 16, 12, 18, 15])
etudiant2 = Etudiant("Mbeki", 22, [10, 11, 9, 13])
etudiant3 = Etudiant("Lamine", 21, [18, 19, 17, 20])

Etudiant.afficher_tous()
Etudiant.nombre_etudiants()
Etudiant.meilleur_notes()
print(Etudiant.moyenne())