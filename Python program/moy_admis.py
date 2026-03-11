def cal_moyenne(a,b,c):
    moy = (a+b+c)/3
    return moy

def admis(moyenne):
    if moyenne >=10:
        return True
    else:
        return False
    
def resultat(name,moy,admis):
    print("---Result---")
    print("Nom :",name)
    print("Moyenne :",moy)
    if admis:
        print("Status admis")

    else:
        print("Statut refuse")

name = input("Entrez votre nom: ")
a = float(input("Entrez la note 1: "))
b = float(input("Entrez la note 2: "))
c = float(input("Entrez la note 3: "))

moy = cal_moyenne(a,b,c)
admis= admis(moy)
resultat(name,moy,admis)