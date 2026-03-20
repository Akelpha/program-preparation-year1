texte = "Python est un langage de programmation flexible."
print(len(texte))
print(texte.upper())
print(texte.lower())
print(texte.find("programmation"))
print(texte.replace("flexible","extraordinaire"))
mots=texte.split()
print(mots)
print(texte.count("e"))
print(texte.startswith("Python"))
print(texte.endswith("flexible"))
phrase = mots[:2]+mots[-2:]
print(" ".join(phrase))