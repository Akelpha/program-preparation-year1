//TD3:EX6 Écrire un programme qui affiche la table de multiplication pour les nombres 1 à 9.

#include <stdio.h>
#include <stdlib.h>

int main(){
     
     
    // printf("Enter your multiplcation tablet number.\n");
    // scanf("%d",&n);
    // for(int i=0;i<=10;i++){
    //     ans = n*i;
    //     printf("%d multiplies by %d = %d\n",n,i,ans);
    // }

    for(int i = 1;i<=9;i++){
        for(int j= 1; j<=9;j++){
            int ans = i*j;
            printf("%d multiply by %d = %d\n",i,j,ans);
        }
    }
    return 0;
}