
class Etudiant:
    def __init__(self, name, firstname,matricule,age,birthday,school):
        self.name = name
        self.firstname = firstname
        self.__matricule = matricule 
        self.__age = age
        self.school = school
        self.birthday = birthday
        self.notes = []

    def getMatricule(self):
        return self.__matricule

    def setMatricule(self,newmatricule):
        self.__matricule = newmatricule
    def getAge(self):
        return self.__age
    def setAge(self,newage):
        # today = datetime.date.today()
        # if self.birthday < today:
        #     self.__age +=1
        # newage = self.__age
         self.__age= newage
    def moyenne(self):
       note = int(input("Inserez vos notes pour chaque cours!"))
       self.notes.append(note)
       moy = sum(self.notes)/len(self.notes)
       return moy
    @staticmethod
    def rattrape(moyenne):
        if moyenne < 10 :
            print("Vous etes en rattrapage.")
        else:
            print("Vous n'allez pas en rattrage.")

    
    def affiches_infos(self,moyenne):
        print("Voici vos informations d'etudiant.")
        print("Votre Nom",self.name)
        print("Votre Prenom:",self.firstname)
        print("Votre Ecole:",self.school)
        print("Votre Matricule:",self.getMatricule)
        print("Votre moyenne:",moyenne)
        print(self.rattrape)


class GestionEtud(Etudiant):
    def __init__(self, name, firstname, matricule, age, birthday, school,classroom,fiche):
        super().__init__(name, firstname, matricule, age, birthday, school)
        self.classRoom = []
        self.fiche = fiche

        





