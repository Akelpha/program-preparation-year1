"""Ecrire une fonction compteMots(phrase) qui renvoie le nombre de mots contenus dans la phrase "phrase". On considère comme mots les ensembles de caractères inclus entre des espaces."""


# print(phrase)
def compteMots(phrase):
    compt = 0
    for i in range(len(phrase)):
        if phrase[i] != ' ' and (i == 0 or phrase[i-1] == ' '):
            compt +=1
    return compt

c = input("Enter a phrase: ")
print(compteMots(c))
