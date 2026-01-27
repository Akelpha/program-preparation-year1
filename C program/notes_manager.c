/*🔹 PROJET C : Student Grade Management System
🧩 Description
Tu écris un programme qui :
✔️ demande le nombre des cours de l'étudiant
✔️ stocke leurs notes dans un tableau
✔️ propose un menu avec plusieurs options
Menu:
1. Saisir les notes
2. Afficher les notes
3. Calculer la moyenne
4. Afficher la meilleure note
5. Afficher les notes supérieures à la moyenne
0. Quitter


*/

#include <stdio.h>
#include <stdlib.h>

void saisirNotes(float T[],int N){
    for(int i=0;i<N;i++){
      printf("Enter your notes.\n");
      scanf("%f",&T[i]);
    }
}
void afficheNotes(float T[],int N){
    printf("Vos notes sont : ");
    for(int i=0;i<N;i++){
        printf("%.2f",T[i]);
    }
    printf("\t");
}

int moyenne(float T[],int N){
    float sum,moy;
    int nbr_cours;
    sum =0;

    for(int i=0;i<N;i++){
        sum=+T[i];
        nbr_cours++;
    }
    moy=sum/nbr_cours;
    return moy;
}
