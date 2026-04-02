"""Ecrire un programme Python qui permet de regrouper dans une liste les mots communs à
deux chaines s1 et s2."""

s1 = input("Enter a phrase 1").split()
s2 = input("Enter a phrase 2").split()
communWord = []
print(s1,s2)
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            communWord.append(s1[i] or s2[j])

print(communWord)