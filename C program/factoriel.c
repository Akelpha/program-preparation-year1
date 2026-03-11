// TD3:EX3 Écrire un programme qui calcule et affiche la factorielle d’un nombre saisi par l’utilisateur.

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, fact;

    fact = 1;
    printf("Enter a number.\n");
    scanf("%d", &n);
    if(n==0){
            fact = 1;
        }
    for (int i = 1; i <= n; i++)
    {
        
        fact = fact * i;
    }
    printf("the factorial of %d is %d.", n, fact);
    return 0;
}