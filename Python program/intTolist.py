L= []
L1= []
L2= []

numb= int(input("Enter the wanted number of interger: "))
for i in range(numb):
    y = int(input("Enter a integer: "))
    L.append(y)
for x in L:
    if x not in L1:
        L1.append(x)
for x in L1:
    L2.append(L.count(x))
L1.sort()
print(L1)
print(L2)
