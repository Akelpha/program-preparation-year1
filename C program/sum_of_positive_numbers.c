// TD3:EX5 Écrire un programme qui affiche les diviseurs d’un entier positif n non nul.

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, div;
    do
    {
        printf("Enter a number.\n");
        scanf("%d", &n);
    } while (n <= 0);

    for (int i = 1; i <= n; i++)
    {
        div = n % i;
        if (div == 0)
        {
            printf("%d \t", i);
        }
    }
    return 0;
}