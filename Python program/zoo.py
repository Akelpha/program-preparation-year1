class Animal:
    def __init__(self,espece,nom,age,sante):
        self.__espece = espece
        self.__nom = nom 
        self.__age = age 
        self.__sante = sante 

    def getNom(self):
        return self.__nom
    
    def setNom(self,newName):
        self.__nom = newName

    def getEspece(self):
        return self.__espece
    
    def setEspece(self,newEspece):
        self.__espece = newEspece

    def getAge(self):
        return self.__age
    
    def setAge(self,newAge):
        self.__age = newAge

    def getHealth(self):
        return self.__sante
    
    def setHealth(self,newHealth):
        self.__sante= newHealth

    def cri(self):
        return f"{self.__name} pousse un cri"
    
    def mager(self):
        return f"{self.__nom} a mangé ."
    
    def verifieSante(self):
        if self.__sante <= 40 :
            return f"{self.__nom} est malade et doit etre soigne"
        
        elif self.__sante <= 70:
            return f"{self.__nom} est moyennement en bonne sante"
        
        else:
           return f"{self.__nom} est en bonne sante"
        


        
class lion(Animal):
    def __init__(self,nom,age,sante):
        super().__init__("Lion",nom,age,sante)
       
    def lanceCri(self):
        return f"{self.getNom()} rugit."

class girafe(Animal):
    def __init__(self,nom,age,sante):
        super().__init__("girafe",nom,age,sante)
        
    def lanceCri(self):
        return f" {self.getNom()} pousse un cri"
    
class zebre(Animal):
    def __init__(self,nom,age,sante):
        super().__init__("zebre",nom,age,sante)
        
    def lanceCri(self):
        return f" {self.getNom()} hennit"
    
class Enclos:
    def __init__(self,taille,emplacement,capacite,liste_Animaux):
        self.__taille = taille
        self.__emplacement = emplacement
        self.__capacite = capacite
        self.___Animaux= []
    def getTaille(self):
        return self.__
    def setTaille(self,newTaille):
        self.__nom = newTaille
    def getAttribute(self):
        return f"Sa taille est: {self.__taille},Son emplacement: {self.__emplacement},Sa capacite: {self.__capacite}"
    def setAttribute(self,newTaille,newemplacement,newCapacite):
        self.__taille = newTaille
        self.__emplacement = newemplacement
        self.__capacite = newCapacite
    def ajouter_animaux(self,animal)
        
class Gardien:
    def __init__(self,nom,age,experience):
        self.nom = nom 
        self.age = age
        self.experience = experience
    def nourir_animaux(self,animaux):
        return f"les animaux ont ete nouris"
        for animal in animaux:
            animal.manger()

class Visiteur:
    def __init__(self,nom,age,billet_entree):
        self.nom = nom
        self.age = age
        self.billet_entree =billet_entree
    def visiter_enclos(self,enclos):
        print()
        if self.__billet_entree:
            print()
            for animal in enclos.get.animaux()
                animal.cri()
        else:
            print()
class Zoo:
    