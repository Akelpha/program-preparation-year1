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
        return f"{self.__nom} pousse un cri"
    
    def manger(self):
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
    def __init__(self,taille,emplacement,capacite):
        self.__taille = taille
        self.__emplacement = emplacement
        self.__capacite = capacite
        self.___Animaux= []
    def getTaille(self):
        return self.__taille
    def setTaille(self,newTaille):
        self.__taille = newTaille
    def getEmplacement(self):
        return self.__emplacement
    def setEmplacement(self,newemplacement,):
        self.__emplacement = newemplacement
    def getCapacite(self):
        return self.__capacite
    def setCapacite(self,newCapacite):
        self.__capacite = newCapacite
    def get_Animaux(self):
        return self.___Animaux
    def ajouter_animaux(self,animal):
        if len(self.___Animaux) < self.__capacite:
            self.___Animaux.append(animal)
            print(f"{animal.getNom()} a été ajouté à l'enclos {self.__emplacement}.")
        else:
            print(f"L'enclos {self.__emplacement} est plein!")
    def nettoyer_Enclos(self):
        print(f"L'enclos {self.__emplacement} a ete nettoyé !")

        
class Gardien:
    def __init__(self,nom,age,experience):
        self.__nom = nom 
        self.__age = age
        self.__experience = experience

    def get_nom(self):
        return self.__nom

    def get_age(self):
         return self.__age

    def get_experience(self):
        return self.__experience

    def set_nom(self, nom):
        self.__nom = nom

    def set_age(self, age):
     self.__age = age

    def set_experience(self, experience):
     self.__experience = experience 
    def nourrir_animaux(self,animaux):
        print(f"les animaux ont ete nouris")
        for animal in animaux:
            animal.manger()

class Visiteur:
    def __init__(self,nom,age,billet_entree):
        self.__nom = nom
        self.__age = age
        self.__billetEntree = billet_entree
    def get_nom(self):
        return self.__nom

    def get_age(self):
         return self.__age

    def get_billetEntree(self):
        return self.__billetEntree

    def set_nom(self, nom):
        self.__nom = nom

    def set_age(self, age):
     self.__age = age 
    def set_billet_entree(self, billet_entree):
        self.__billet_entree = billet_entree
  
    def visiter_enclos(self,enclos):
        print(f"{self.__nom} visite l'enclos situé {enclos.getEmplacement()}")
        if self.__billetEntree:
            print("Le billet est valide. Les animaux font leurs cris :")
            for animal in enclos.get_Animaux():
                animal.cri()
        else:
            print(f"{self.__nom} n'a pas de billet d'entrée valide.")
class Zoo:
    def __init__(self,nom):
        self.__nom = nom
        self.__enclos = []
        self.__animaux = []
        self.__gardiens = []
        self.__visiteurs = []
    def ajouter_enclos(self,enclos):
        self.__enclos.append(enclos)
        print("Enclos ajouté au zoo")
    def supprimer_Enclos(self,enclos):
        if enclos in self.__enclos:
            self.__enclos.remove(enclos)
            print("Enclos supprimé du zoo")
    def ajouter_animal(self,animal):
        self.__animaux.append(animal)
        print("Animal ajouté au zoo.")
    def supprimer_animal(self,animal):
        if animal in self.__animaux:
            self.__animaux.remove(animal)
            print(f"{animal.getNom()} a été supprimé du zoo")
    def ajouter_gardien(self,gardien):
        self.__gardiens.append(gardien)
        print(f"Le Gardien {gardien.get_nom()} a été ajouté au zoo")
    def supprimer_gardien(self,gardien):
        if gardien in self.__gardien:
            print(f"Le Gardien {gardien.getNom()} a été supprimé au zoo")
    def ajouter_visiteur(self,visiteur):
        self.__visiteurs.append(visiteur)
        print(f"Le visiteur {visiteur.get_nom()} a été ajouté au zoo.")
    def supprimer_visiteur(self,visiteur):
        if visiteur in self.__visiteurs:
            self.__visiteurs.remove(visiteur)
            print(f"{visiteur.getNom()} a été supprimé du zoo")
    def simuler_journee(self):
        print(f"\n==============================")
        print(f"Simulation d'une journée au zoo : {self.__nom}")
        print(f"==============================")

# Nourrir les animaux
        print("\n1. Nourrir les animaux")
        for gardien in self.__gardiens:
            gardien.nourrir_animaux(self.__animaux)

# Nettoyer les enclos
        print("\n2. Nettoyer les enclos")
        for enclos in self.__enclos:
            enclos.nettoyer_Enclos()

        # Vérifier la santé des animaux
        print("\n3. Vérifier la santé des animaux")
        for animal in self.__animaux:
            animal.verifieSante()

        # Visite des visiteurs
        print("\n4. Visite des visiteurs")
        for visiteur in self.__visiteurs:
            for enclos in self.__enclos:
                visiteur.visiter_enclos(enclos)
# Création des animaux
lion1 = lion("Simba", 5, 90)
girafe1 = girafe("Gigi", 7, 75)
zebre1 = zebre("Zaza", 4, 55)

# Création des enclos
enclos_savane = Enclos("Grand", "Zone Savane", 3)
enclos_foret = Enclos("Moyen", "Zone Forêt", 2)

# Ajouter les animaux aux enclos
enclos_savane.ajouter_animaux(lion1)
enclos_savane.ajouter_animaux(girafe1)
enclos_savane.ajouter_animaux(zebre1)

# Création d'un gardien
gardien1 = Gardien("Ahmed", 35, 10)

# Création des visiteurs
visiteur1 = Visiteur("Youssef", 20, True)
visiteur2 = Visiteur("Sara", 18, False)

# Création du zoo
zoo = Zoo("Zoo de Fès")

# Ajouter les éléments au zoo
zoo.ajouter_animal(lion1)
zoo.ajouter_animal(girafe1)
zoo.ajouter_animal(zebre1)

zoo.ajouter_enclos(enclos_savane)
zoo.ajouter_enclos(enclos_foret)

zoo.ajouter_gardien(gardien1)

zoo.ajouter_visiteur(visiteur1)
zoo.ajouter_visiteur(visiteur2)

# Simulation d'une journée
zoo.simuler_journee()