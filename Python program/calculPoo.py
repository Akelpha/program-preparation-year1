class Calcul :
    def __init__(self):
        pass
    @staticmethod
    def factorielle(n):
        if n==1 or n==0:
            return 1
        else:
            return n*Calcul.factorielle(n-1)
    @staticmethod
    def somme(n):
        if n==1:
           return 1
        else:
            return n+Calcul.somme(n-1)
        
    @staticmethod
    def testPrim(n):
        
        
