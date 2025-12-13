// Écrire un programme qui demande à l'utilisateur de saisir deux données numériques et qui échange leurs contenus si elles sont de même signe, sinon il met la somme des deux dans la première donnée et leur produit dans la seconde.

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int A, B, new_A, new_B;
    printf("Enter your two numbers(A and B).\n");
    scanf("%d %d", &A, &B);
    new_A = A;
    new_B = B;
    if (A * B > 0)
    {
        new_A = B;
        new_B = A;
        printf("The new value of A is %d and B is %d", new_A, new_B);
    }
    else if (A * B == 0)
    {
        new_A = A;
        new_B = B;
        printf("The new value of A is %d and B is %d", new_A, new_B);
    }
    else
    {
        new_A = A + B;
        new_B = A * B;
        printf("The new value of A is %d and B is %d", new_A, new_B);
    }
    return 0;
}