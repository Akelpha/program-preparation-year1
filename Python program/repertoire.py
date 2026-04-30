"""On considère les données suivantes :
Créer un dictionnaire qui s’appelle répertoire qui associe les noms aux numéros de téléphone.
Comment accéder au téléphone de Noura ?
Comment savoir si "Fatima” est enregistrée dans le répertoire ?
Modifier le numéro de Marie, il se termine par un 9 et non un 1.
Ajouter “Rania” dont le numéro est “0789898989”
Supprimer “Hanae” du répertoire.
Afficher tous les éléments du dictionnaire, ainsi que les clés et les valeurs."""


repectoire = {
    "Marie": "0687654321",
    "Hanae": "0708554733",
    "Anas": "0744394810",
    "Noura": "0614656812"
}

print(repectoire["Noura"])
if "Fatima" in repectoire:
      print("Fatime se trouve dans le repertoire")
else:
      print("Fatime ne se trouve pas dans le repertoire")

repectoire["Marie"]="0687654329"
repectoire["Rania"]="0789898989"
print(repectoire)
del repectoire["Hanae"]
#this
for key,value in repectoire.items():
      print(key, ":", value)


