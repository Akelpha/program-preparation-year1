"""Exercice 1 :Constituez une liste semaine contenant les 7 jours de la semaine. - À partir de cette liste,
comment récupérez-vous seulement les 5 premiers jours de la semaine d'une part, et ceux
du week-end d'autre part ? Utilisez pour cela l'indiçage. - Cherchez un autre moyen pour
arriver au même résultat (en utilisant un autre indiçage). - Trouvez deux manières pour
accéder au dernier jour de la semaine. - Inversez les jours de la semaine en une commande."""

WeekList = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(WeekList[ : 5: ])
print(WeekList[ -3: : 1])
print(WeekList[-2: : ])
print(WeekList[ 4: : ]) 
print(WeekList[ : : -1])