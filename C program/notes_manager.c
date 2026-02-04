/*🔹 PROJET C : Student Grade Management System
🧩 Description
Tu écris un programme qui :
✔️ demande le nombre des cours de l'étudiant
✔️ stocke leurs notes dans un tableau
✔️ propose un menu avec plusieurs options
Menu:
1. Saisir les notes✔️
2. Afficher les notes✔️
3. Calculer la grade_point_average✔️
4. Afficher la meilleure note✔️
5. Afficher les notes supérieures à la grade_point_average✔️
0. Quitter✔️
Cours	Note
Math	15.5
Phys	12.0
Chim	18.0
Info	14.5
Anglais	16.0

*/

#include <stdio.h>
#include <stdlib.h>
// 1. Saisir les notes
void saisirNotes(float T[], int N)
{
    for (int i = 0; i < N; i++)
    {
        printf("Enter your notes.\n");
        scanf("%f", &T[i]);
    }
}
// 2. Afficher les notes
void afficheNotes(float T[], int N)
{
    printf("Vos notes sont : ");
    for (int i = 0; i < N; i++)
    {
        printf("%.2f ", T[i]);
    }
    printf("\t");
}
// 3. Calculer la grade_point_average
float grade_point_average(float T[], int N)
{
    float sum;
    sum = 0;

    for (int i = 0; i < N; i++)
    {
        sum += T[i];
    }

    return sum / N;
}
// 4. Afficher la meilleure note
float bestNotes(float T[], int N)
{
    int imax = 0;

    for (int i = 0; i < N; i++)
    {

        if (T[i] > T[imax])
        {
            imax = i;
        }
    }
    return T[imax];
}
// 5. Afficher les notes supérieures à la grade_point_average
float SupNoteMoy(float T[], int N)
{
    float moy = grade_point_average(T, N);
    int c = 0;
    for (int i = 0; i < N; i++)
    {
        if (T[i] > moy)
        {
            printf("%2.f ", T[i]);
            c++;
        }
    }

    if (c == 0)
    {
        printf("There are no notes above the average.\n");
    }

    printf("\n");
    return c;
}

// La fonction principale
int main()
{
    int N;
    int choice;
    printf("Enter the tab length.\n");
    scanf("%d", &N);
    float T[N];
    do
    {
        printf("\nMenu:\n1. Saisir les notes\n2. Afficher les notes\n3. Calculer GPA\n4. Meilleure note\n5. Notes > GPA\n0. Quitter\n");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            saisirNotes(T, N);
            break;
        case 2:
            afficheNotes(T, N);
            break;
        case 3:
            printf("Your GPA is %2.f \n", grade_point_average(T, N));
            break;
        case 4:
            printf("Your best note is %2.f \n", bestNotes(T, N));
            break;
        case 5:
             SupNoteMoy(T, N);
            break;
        case 0:
            printf("Bye!! Thanks\n");
        default:
            printf("Invalid choice.\n");
            break;
        }
    } while (choice < 6);
    return 0;
}