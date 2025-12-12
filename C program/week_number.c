// Écrire un programme en C qui permet de demander à l'utilisateur de saisir un entier entre 1 et 7 au clavier, et affiche le nom du jour correspondant.

#include <stdio.h>
#include <stdlib.h>


int main (){
    int number;

    printf("Enter a number between 1 and 7\n");
    scanf("%d",&number);
    switch (number)
    {
    case 1:
        printf("Monday");
        break;
    case 2:
        printf("Tuesday");
        break;
    case 3:
        printf("Wednesday");
        break;
    case 4:
        printf("Thursday");
        break;
    case 5:
        printf("Friday");
        break;
    case 6:
        printf("Saturday");
        break;
    case 7:
        printf("Sunday");
        break;
    
    default: printf("This is not a week day.\n");
        break;
    }
    return 0;
}