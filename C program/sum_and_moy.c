// Écrire un programme en C qui demande à l'utilisateur de saisir 15 réelles qu’on stocke dans un tableau T. Ensuite, calcule et affiche la moyenne des nombres saisies au tableau, puis détermine et affiche le maximum des éléments du tableau T.

#include <stdio.h>
#include <stdlib.h>

int main(){
    float T[15],sum,moy;
    int imax;
    imax=1;
    sum=0;
    for(int i=0;i<15;i++){
        printf("Entrer l'element T[%f]:",i+1);
        scanf("%f",&T[i]);
        sum=sum+T[i];
        if(T[i]>T[imax]){
            imax=i;
        }
    };
    moy=sum/15;
    printf("La moyenne et la maximum des elements du tableau sont %f et %f",moy,T[imax]);
}