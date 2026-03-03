"""Un palindrome est un mot dont l'ordre des lettres reste le même si on le lit de gauche à droite ou de droite à gauche. Par exemple : 'laval', 'radar, 'sos'... sont des palindromes. Ecrire un programme en Python qui demande à l'utilisateur de saisir un mot et de lui renvoyer s'il s'agit d'un palindrome ou non ?"""


c = input("Enter a word: ")
inverseWord = c[-1::-1]
if c == inverseWord:
    print("C'est un palindrome")
else: 
    print("Ce n'est pas un palindrome")