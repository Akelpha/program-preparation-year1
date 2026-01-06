//TD3:EX6 Écrire un programme qui affiche la table de multiplication pour les nombres 1 à 9.

#include <stdio.h>
#include <stdlib.h>

int main(){
     int n,ans;
     
    printf("Enter your multiplcation tablet number.\n");
    scanf("%d",&n);
    for(int i=0;i<=10;i++){
        ans = n*i;
        printf("%d multiplies by %d = %d\n",n,i,ans);
    }
    return 0;
}