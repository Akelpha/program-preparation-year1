class Etudiant:
    listE=[]
    def __init__(self,nom,age,note):
        self.nom=nom
        self.age=age
        self.nom=note
        Etudiant.listE.append(self)
    
    @classmethod
    def afficher_tous(cls):
        for x in cls.listE:
            print(x.nom,x.age,x.note)
    @classmethod
    def nombre_etudiants(cls):
        print(len(cls.listE))
    @classmethod
    def meilleur_notes(cls):
        meilleur = max(cls.listE, key = lambda x: x.note)
        print(meilleur.nom,meilleur.note)

    @classmethod
    def moyenne(cls):
        for x in cls.listE:
            s+=x.note
            # s = sum([e.note for e in cls.listE])
        return s/len(cls.listE)
    



Etudiant.afficher_tous()
Etudiant.nombre_etudiants()
Etudiant.meilleur_notess()
Etudiant.moyenne()