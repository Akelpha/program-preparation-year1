// Ecrire un algorithme qui affiche les couleurs.
#include <stdio.h>
#include <stdlib.h>


int main (){
    int num_color;
    printf("Inserer un chiffre entre 1 et 7\n");
    scanf("%d",&num_color);
    switch (num_color)
    {
    case 1:
        printf("Rouge");
        break;
    case 2:
        printf("Jaune");
        break;
    case 3:
        printf("Bleu");
        break;
    case 4:
        printf("Bleu");
        break;
    case 5:
        printf("Rose");
        break;
    case 6:
        printf("Mauve");
        break;
    case 7:
        printf("Noir");
        break;
    
    default: printf("Ceci ne correspont a aucune couleur");
        break;
    }
    return 0;
}