/*TD2:Ex6 Les habitants d'une ville paient l'impôt selon les règles suivantes :
- Les hommes de plus de 20 ans paient l'impôt
- Les femmes paient l'impôt si elles ont entre 18 et 35 ans
- Les autres ne paient pas d'impôt
Écrire un programme qui demande l'âge et le sexe d'un habitant et affiche si celui-ci est imposable
ou non imposable.*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    char sex;
    int age;
    printf("Enter your age and your sex(M OR W).\n");
    scanf("%d %c", &age, &sex);
    if (sex == 'M' && age > 20)
    {
        printf("You have to pay the taxes.\n");
    }
    else if (sex == 'W' && (age >= 18 && age <= 35))
    {
        printf("You have to pay the taxes.\n");
    }
    else
    {
        printf("You don't have to pay the taxes.\n");
    }

    return 0;
}