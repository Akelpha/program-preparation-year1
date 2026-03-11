// I will try to create a calculator app to see if i have understand my C courses .

#include <stdio.h>
#include <stdlib.h>

int addition(int a, int b)
{

    return a + b;
}
int soustration(int a, int b)
{
    ;
    return a - b;
}
int multiplication(int a, int b)
{

    return a * b;
}
int division(int a, int b)
{

    return a / b;
}
int main()
{
    int a, b;
    char operateur;
    printf("Enter your numbers.\n");
    scanf("%d %d", &a, &b);
    printf("Enter your operation.\n");
    scanf(" %c", &operateur);
    switch (operateur)
    {
    case '+':
        printf("Result = %d\n", addition(a, b));
        break;
    case '-':
        printf("Result = %d\n", soustration(a, b));

        break;

    case '*':
        printf("Result = %d\n", multiplication(a, b));

        break;
    case '/':
        if (b != 0)
        {
            printf("Result = %d\n", division(a, b));
        }
        else
        {
            printf("Impossible.\n");
        }

        break;
    default:
        printf("This operation doesn't exist.\n");
        break;
    }
    return 0;
}