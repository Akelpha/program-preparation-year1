"""Écrire une fonction qui prend une phrase en paramètre et affiche les mots écrits en
majuscules dans la phrase."""

def countUpper(phrase):
    phraseList = phrase.split()
    for x in phraseList:
        if x.isupper() == True:
            print(x)

phrase = input("Enter a phrase: ")
countUpper(phrase)