def remplacer(chaine):
    return chaine[0] + chaine[1:].replace(chaine[0],'@')
    """newChaine = premier
    for i in range(1,len(chaine)):
        if chaine[i]== premier:
            newChaine +='@'
        else:
            newChaine +=chaine[i]
    return newChaine"""

chaine = input("Enter a string: ")
print(remplacer(chaine))