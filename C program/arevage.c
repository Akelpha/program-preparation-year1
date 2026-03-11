// TD3:EX1 :Écrire un programme en C qui lit 30 valeurs réelles et qui détermine la moyenne des valeurs.

#include <stdio.h>
#include <stdlib.h>

int main()
{
    float n, sum, moy;

    sum = 0;
    for (int i = 0; i < 30; i++)
    {
        printf("Enter a real value. \n");
        scanf("%f", &n);
        sum = sum + n;
    }
    moy = sum / 30;
    printf("the arevage is %f",moy);
    return 0;
}