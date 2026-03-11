// TD1:Ex4 Écrire un programme qui demande à l'utilisateur de saisir les notes de 4 matières d'un étudiant et de saisir les coefficients correspondants à chaque matière, puis le programme calcule la moyenne des 4 notes et affiche la moyenne finale de l'étudiant avec 2 chiffres après la virgule.

#include <stdio.h>
#include <stdlib.h>

int main(){
    int note1,note2,note3,note4,coe1,coe2,coe3,coe4,total_coe;
    float moyenne_note,moyenne_finale;

    printf("Entrez les notes de vos 4 matieres.\n");
    scanf("%d %d %d %d",&note1,&note2,&note3,&note4);
    printf("Entrez les coefficients correspondants a chaque matiere.\n");
    scanf("%d %d %d %d",&coe1,&coe2,&coe3,&coe4);

    moyenne_note = (note1*coe1)+(note2 * coe2)+(note3 * coe3)+(note4 * coe4);
    total_coe = coe1+coe2+coe3+coe4;
    moyenne_finale = moyenne_note / total_coe;
    printf("La moyenne total est de %.2f",moyenne_finale);
    return 0;
}
