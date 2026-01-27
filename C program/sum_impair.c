/*Ecrire les fonctions suivantes :
Afficher qui permet d’afficher les N composantes du tableau T.
Sum_impair qui affiche la somme des nombres impairs existant dans le tableau.
Remplace qui remplace dans le tableau tous les nombres pairs par 16.
Ecrire un programme principal qui lit la dimension N d'un tableau T (de type int), remplit le tableau par des valeurs entrées au clavier et teste toutes les fonctions définies précédemment.*/

#include <stdio.h>
#include <stdlib.h>

void afficher(int T[],int N){
    for(int i=0;i<N;i++){
        printf("%d ", T[i]);
    }
   printf("\n");
}
int Sum_impair(int T[],int N){
   int sum=0;
   for(int i=0;i<N;i++){
    if(T[i] % 2 !=0){
        sum =+T[i];
    }
   }
   return sum;
}
void remplace (int T[],int N){
    for(int i=0;i<N;i++){
    if(T[i] % 2 ==0){
        T[i] = 16;
    }
   }
   afficher(T,N);
}


int main(){
    int N,T[100];
    printf("Enter the tab length.\n");
    scanf("%d",&N);
    for(int i=0;i<N;i++){
        scanf("%d",&T[i]);
    }
    afficher(T,N);
    printf("La sum est %d \n",Sum_impair(T,N));
    printf("Le nouveau tableau est :");
    remplace(T,N);
    return 0;
}
