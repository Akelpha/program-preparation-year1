def moyenne_notes(classe):
    moyennes = {}
    for eleve,notes in classe.items():
        s=sum(notes.values())
    moyennes = s/len(notes)
    return moyennes

classe = {"Keren":{"Electronique":18,"Francais":17,"Analyse":16,"Anglais":14},"Theo":{"Electronique":18,"Francais":14,"Analyse":15,"Anglais":20},"Christina":{"Electronique":17,"Francais":20,"Analyse":18,"Anglais":15}}
print(moyenne_notes(classe))