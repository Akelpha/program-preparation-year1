# L1 = []
# L2 = []
# L3 = []
# for i in range(3):
#     x= input("Enter the name of the student")
#     L1.append(x)
#     y = int(input("Enter the first note"))
#     L2.append(y)
#     z = int(input("Enter the second note"))
#     L3.append(z)
# for x,y,k in zip(L1,L2,L3):
#     # S = sum(y,z)
#     print(f"{x} a  obtenu :{(y+z)/2}")
def analyse(liste):
     S=sum(liste)
     maxi = max(liste)
     mini  =min(liste)
     L= sorted(liste)
     print(f"{S},{maxi},{mini},{L}")

liste = [12,13,15,167,43,89,54,73,23]
analyse(liste)
