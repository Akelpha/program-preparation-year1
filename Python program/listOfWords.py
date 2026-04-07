liste1 = ["hello", "world!", ["good", "morning"], "python", ["is", "awesome",["and", "fun" ]]]


def listToString(L):
    liste2 = []
    for x in L: 
        if type(x) == list:
            liste2.extend(listToString(x))
        elif type(x) == str:
            liste2.append(x)
    
    return liste2
phrase = " ".join(listToString(liste1))
print(listToString(liste1))
print(phrase)
