Ltrie = []

def listImbrique(List1,List2):
    for i in range(len(List1)):
        for j in range(len(List2)):
            if (type(List1[i]) and type(List2[j]) == list) and (List1[i] == List2[j]):
                Ltrie.append(List1[i] or List2[j])
                Ltrie.sort(key=len)
    return Ltrie



list1 =[[1,2,3],[1,2,23,4],1,3]
list2= [[1,2,3],[1,2,23,4],32]
print(listImbrique(list1,list2))