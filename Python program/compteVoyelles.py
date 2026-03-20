def voyelle(chaine):
    voyelles="aeiouy"
    nbre = 0
    for v in voyelles:
        nbre +=chaine.count(v)

    return nbre

chaine = input("Enter a string").lower()
print(voyelle(chaine))

