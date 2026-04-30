"""Écrire une fonction qui prend en argument un tuple composé de nombres entiers et renvoie un tuple
contenant le plus grand des entiers et le plus petit."""

def minMaxTuple(T):
    Tm =(max(T),min(T))
    return Tm

t=(10, 5, 20, 3, 15)
print(minMaxTuple(t))