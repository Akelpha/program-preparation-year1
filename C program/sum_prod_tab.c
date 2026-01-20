// Écrire un algorithme qui demande à l'utilisateur de saisir 10 réels stockés dans un tableau, afficher tout le tableau rempli, puis l’algorithme calcule et affiche la somme et le produit des éléments du tableau.

#include <stdio.h>
#include <stdlib.h>

int main(){
    float tab[10],sum,prod;
    sum=0;
    prod=1;
    for(int i=0;i<10;i++){
        printf("Enter a real value.\n");
        scanf("%f",&tab[i]);
        sum=+tab[i];
        prod=prod*tab[i];
    }
    printf(" La somme et le produit sont %f et %f \n",sum,prod);
    printf("These are the tab's element :");
    for(int l=0;l<10;l++){
         printf("These are the tab's element : %2.f \t",tab[l]);
    }
    return 0;
}