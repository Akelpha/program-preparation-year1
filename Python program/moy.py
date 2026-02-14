# Ecire un programme qui lit 20 valeurs reeles et qui determine la moyenne des valeurs strictements positifs et la moyenne des valeurs strictement negatifs

sumneg = 0
negnumber =0
sumpos = 0
posnumber =0
for i in range(0,20,1):
    a = float(input("Entrez un reel : "))

    if(a<0):
        sumneg = sumneg + a
        negnumber +=1
        moyneg = sumneg/negnumber

    elif(a>0):
        sumpos = sumpos + a
        posnumber +=1
        moypos = sumpos/posnumber
    else:
        moyneg =0
        moypos =0
    
print("la valeur de la moyenne des nombres positif est ",moypos," et des nombres negatifs est ",moyneg)
