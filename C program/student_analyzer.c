/* 🚀 PROJET PRINCIPAL (niveau sérieux)
🎓 Student Performance Analyzer
Tu écris un programme qui gère :
✔️ plusieurs matières
✔️ plusieurs notes par matière
✔️ des statistiques intelligentes
1. Saisir les notes✔️
2. Afficher toutes les notes✔️
3. Moyenne par matière
4. Moyenne générale
5. Meilleure note (globale)
6. Matière la plus difficile (moyenne la plus basse)
0. Quitter

📘 Tableau des notes
Matière	Notes
0 (Math)	12 · 14 · 10 · 16 · 8
1 (Physique)	15 · 13 · 14 · 12 · 16
2 (Informatique)	18 · 17 · 19 · 16 · 20
3 (Chimie)	9 · 11 · 10 · 8 · 12
*/
/* int main(void){
    int Tab[3][4] = {{0,1,2,3}, {4,5,6,7}, {8,9,10,11}};
    int i,j;

    for(i=0 ; i< 3 ; i++)
    {
        for(j=0 ; j < 4 ; j++)
        {
            printf(" Elément : Tab[%d][%d]= %d \n", i, j, Tab[i][j]);
        }
    }


    return 0;
} */

#include <stdio.h>
#include <stdlib.h>

void saisirNotes(int M, int N, float T[][N])
{
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            scanf("%f", &T[i][j]);
        }
    }
}
void afficheNotes(int M, int N, float T[][N])
{
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            printf(" T[%d][%d]= %d \n", i, j, T[i][j]);
        }
    }
}
float moyenneMatiere(int M, int N, float T[][N])
{
    float sumM = 0;

    for (int j = 0; j < N; j++)
    {
        sumM += T[M][j];
    }

    return sumM / N;
}
float moyenneGen(int M, int N, float T[][N])
{

    float sumGen = 0;
    for (int i = 0; i < M; i++)
    {
        sumGen += moyenneMatiere(i, N, T);
    }

    return sumGen / M;
}
float bestNote(int M, int N, float T[][N])
{
    int imax = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (T[i][j] > T[i][imax])
            {
                imax = j;
            }
        }
    }
    return T[M][imax];
}
float mostDifficultMat(int M, int N, float T[][N])
{
    float difMat = moyenneMatiere(0, N, T);
    for (int i = 1; i < M; i++)
    {
        float moy = moyenneMatiere(i, N, T);
        if (moy < difMat)
        {
            difMat = moy;
        }
    }
    return difMat;
}

int main()
{
    int N, M;

    do
    {
        printf("Enter your courses number (>=2): \n");
        scanf("%d", &M);
    } while (M < 2);

    printf("Enter number of notes per course: ");
    scanf("%d", &N);

    getchar(); // 🔥 VERY IMPORTANT : vide le buffer

    char CName[M][20];

    for (int i = 0; i < M; i++)
    {
        printf("Enter course %d name: ", i + 1);
        fgets(CName[i], 20, stdin);
    }

    // Tableau des notes
    float T[M][N];

    int choice;
    do
    {
        printf("\nMenu:\n1.Saisir les notes\n2.Afficher toutes les notes\n3.Moyenne par matière\n4.Moyenne par matière\n5.Moyenne générale\n6.Matière la plus difficile(moyenne la plus basse)\n0.Quitter\n");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            saisirNotes(M, N, T);
            break;
        case 2:
            afficheNotes(M, N, T);
            break;
        case 3:
            printf("The GPA of %s is %.2f", CName, moyenneMatiere(M, N, T));
            break;
        case 4:
            printf("The GPA general is %.2f", moyenneGen(M, N, T));
            break;
        case 5:
            printf("The best note is %.2f", bestNote(M, N, T));
            break;
        case 6:
            printf("The most difficult course is %.2f", mostDifficultMat(M, N, T));
        case 0:
            printf("Bye!" );
        default:
            printf("Invalid choice.\n");
            break;
        }
    } while (choice < 6);
    return 0;
}
