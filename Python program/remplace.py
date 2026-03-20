def remplacer(chaine):
    premier = chaine[0]
    return premier + chaine[1:].replace(premier,'@')"
    """newChaine = premier
    for i in range(1,len(chaine)):
        if chaine[i]== premier:
            newChaine +='@'
        else:
            newChaine +=chaine[i]
    return newChaine"""

chaine = input("Enter a string: ")
print(remplacer(chaine))