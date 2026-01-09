#include <stdio.h>
#include <stdlib.h>

int main(){
    int n, imax;
    printf("Veuillez entrer la taille du tableau.\n");
    scanf("%d",&n);
    int tab[n];
    imax=1;
    for(int i=0;i<n;i++){
        printf("Enter a value.\n");
        scanf("%d",&tab[i]);
        if(tab[i]>tab[imax]){
            imax=i;
        }
    }
    printf("le plus grand element est %d",tab[imax]);
}