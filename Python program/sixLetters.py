"""Ecrire une fonction qui prend en argument une liste de mots et affiche deux listes ; la
première liste contient les mots de moins de six lettres, la seconde contient les mots de six
lettres ou plus."""

def sixLetters(L):
    aboveSixLetters = []
    belowSixLetters =[]
    for x in L:
        if len(x)>= 6:
            aboveSixLetters.append(x)
        else:
            belowSixLetters.append(x)
    print(aboveSixLetters,belowSixLetters)


words = [
    "ok", "go", "if", "on", "un", "je", "tu", "il",
    "cat", "dog", "sun", "feu", "eau", "air", "mer", "rue",
    "book", "fire", "moon", "chat", "lune", "arbre", "code", "play",
    "chair", "house", "river", "tiger", "piano", "fleur", "nuage",
    "animal", "bridge", "castle", "jardin", "soleil", "papier",
    "brother", "captain", "diamond", "machine", "voiture", "cuisine",
    "absolute", "calendar", "elephant", "mountain", "airplane", "chocolat",
    "adventure", "beautiful", "chocolate", "geography", "ordinateur","absolutely", "discovered", "impossible", "strawberry", "technology","comfortable", "information", "mathematics", "programming", "underground","accomplished", "independence", "intelligence", "satisfaction", "contemporary"
]

sixLetters(words)