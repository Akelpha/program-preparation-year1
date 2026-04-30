result = {}
"""while True:
    etudiant = input("Saisir le nom: ")
    if etudiant == " ":
        break
    notes = int(input("Saisir la note: "))
    result[etudiant] = notes
print(result)"""
n =int(input("Enter the diactionnaire length : "))
for i in range(n):
    etudiant = input("Saisir le nom: ")
    notes = int(input("Saisir la note: "))
    result[etudiant] = notes
print(result)
c = 0
for key,value in result.items:
    print(f"The student {key} got {value}")

for key,value in result.items:
    if value > 15:
        print(f"The student {key} got {value}")
        c+=1
        print(f"The total numbers of student who got notes above 15 is {c}")

print(sum(result.values()))

