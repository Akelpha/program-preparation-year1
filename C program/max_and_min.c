#include <stdio.h>

void saisir(int T[], int N)
{
    int i;
    for (i = 0; i < N; i++)
    {
        printf("T[%d] = ", i);
        scanf("%d", &T[i]);
    }
}
void afficher(int T[], int N)
{
    int i;
    for (i = 0; i < N; i++)
    {
        printf("%d ", T[i]);
    }
    printf("\n");
}
int min(int T[], int N){
    int imin =1;;
    
    for(int i=0;i<10;i++){
               
        
        if(T[i]<=T[imin]){
            imin=i;
        }
    }
    return T[imin];
}
int max(int T[], int N){
    int imax =1;;
    
    for(int i=0;i<10;i++){        
        
        if(T[i]>T[imax]){
            imax=i;
        }
    }
    return T[imax];
}

int main(){
    int N;
    printf("Enter the tab length.\n");
    scanf("%d",&N);

    int T[N];
    saisir(T,N);
    afficher(T,N);
    printf("Le maximun est %d",max(T,N));
    printf("le minimum est %d",min(T,N));
    return 0;
}