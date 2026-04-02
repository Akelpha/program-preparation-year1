"""Etant donnée la liste des notes des élèves :
notes = [12 , 04 , 14 , 11 , 18 , 13 , 07, 10 , 05 , 09 , 15 , 08 , 14 , 16]
Ecrire un programme Python qui permet d'extraire de cette liste et créer une autre liste qui
contient uniquement les notes au-dessus de la moyenne (les notes >=10), et qui permet
d'extraire de la liste une autre liste contenant uniquement les notes inférieures à la moyenne
de toutes ces notes."""


notes = [12 , 4 , 14 , 11 , 18 , 13 , 7, 10 , 5 , 9 , 15 , 8 , 14 , 16]
arevageAb =[]
arevageBel = []
for i in range(len(notes)):
    s = sum(notes)
moyenne = s / len(notes)
for i in range(len(notes)):
    if notes[i] >= moyenne :
          arevageAb.append(notes[i])
    else:
         arevageBel.append(notes[i])
print(arevageAb)
print(arevageBel)