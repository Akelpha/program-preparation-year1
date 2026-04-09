"""Etant donnée la liste des notes des élèves :
notes = [12 , 04 , 14 , 11 , 18 , 13 , 07, 10 , 05 , 09 , 15 , 08 , 14 , 16]
Ecrire un programme Python qui permet d'extraire de cette liste et créer une autre liste qui
contient uniquement les notes au-dessus de la moyenne (les notes >=10), et qui permet
d'extraire de la liste une autre liste contenant uniquement les notes inférieures à la moyenne
de toutes ces notes."""


notes = [12 , 4 , 14 , 11 , 18 , 13 , 7, 10 , 5 , 9 , 15 , 8 , 14 , 16]
above10=[]
arevageBel = []
s = sum(notes)
moyenne = s / len(notes)
for i in range(len(notes)):
    if notes[i] >= 10 :
          above10.append(notes[i])
    elif notes[i]<moyenne:
         arevageBel.append(notes[i])
print(above10)
print(arevageBel)