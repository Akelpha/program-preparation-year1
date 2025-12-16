//TD2:Ex5 Ecrire un programme qui lit trois nombres entiers A, B et C et effectue un tri par ordre décroissant de ces derniers en échangeant leur valeur à l'aide d'une variable AIDE.

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int A, B, C, help;

    printf("Enter your 3 numbers.\n");
    scanf("%d %d %d", &A, &B, &C);

    if (B > A)
    {
        help = A;
        A = B;
        B = help;
    }
    else if (C > B)
    {
        help = B;
        B = C;
        C = help;
    }
    else if (A > C)
    {
        help = C;
        C = A;
        A = help;
    }
    printf("The sort by decreasing is %d, %d, %d.\n", A, B, C);
    return 0;
}