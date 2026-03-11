// Ecrivez un algorithme constituant un tableau, à partir de deux tableaux de même longueur saisis par l’utilisateur. Le nouveau tableau sera la somme des éléments des deux tableaux de départ.

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    printf("Enter the length of your tabs.\n");
    scanf("%d", &n);
    int tab1[n], tab2[n], tabS[n];
    // Remplissage du premier tableau
    printf("Tableau 1 :\n");
    for (int i = 0; i < n; i++)
    {
        printf("Enter a value.\n");
        scanf("%d", &tab1[i]);
    }
    // Remplissage du deuxieme tableau
    printf("Tableau 2 :\n");
    for (int j = 0; j < n; j++)
    {
        printf("Enter a value.\n");
        scanf("%d", &tab2[j]);
    }
    for (int k = 0; k < n; k++) {
       tabS[k] = tab1[k]+tab2[k];
    }
    printf("Tableau des sommes :\n");    
    for (int l = 0; l < n; l++) {       
         printf("%d \t", tabS[l]);    
        }    
    printf("\n");
return 0;

}