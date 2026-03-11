"""Ecrire une fonction compteMots(phrase) qui renvoie le nombre de mots contenus dans la phrase "phrase". On considère comme mots les ensembles de caractères inclus entre des espaces."""


# print(phrase)
def compteMots(phrase):
    compt = 1
    for i in range(len(phrase)):
        if phrase[i] == ' ':
            compt +=1
    return compt

phrase= input("Enter a phrase: ")
print(f"{compteMots(phrase)}")
