"""
🧠 Exercice : Mini système de gestion de notes
Tu dois écrire un programme qui :
Demande à l’utilisateur combien d’étudiants il veut entrer.
Pour chaque étudiant :
Demande son nom
Demande sa note (entre 0 et 20)
Vérifie que la note est valide (sinon redemande)
À la fin :
Affiche la moyenne
Affiche combien ont validé (note ≥ 10)
Affiche le meilleur étudiant
Affiche les étudiants en rattrapage (note < 8)"""

student_number = int(input("Enter the student number: "))
total = 0
count_valid = 0
count_rattrapage =0
for i in range(0,student_number,1):
    name=input("Enter the student name.")
    note = float(input("Enter the student note. "))
    while note < 0 or note > 20:
        note = float(input("Invalid note. Enter the student note again: "))
        if 0 <= note >= 20 : 
            break

    total +=note
    if note >= 10:
        count_valid +=1
    elif note >=8:
        count_rattrapage+=1
    if i == 0:
        best_note = note
        best_noteName = name
    else:
        if note > best_note:
            best_note = note
            best_noteName = name

    

print(f"The GPA general is {total/student_number}")
print(f"the student who validate are {count_valid} and those who are cathing up are {count_rattrapage}") 
print(f"The best student is {best_noteName} and scored {best_note}") 

        
    