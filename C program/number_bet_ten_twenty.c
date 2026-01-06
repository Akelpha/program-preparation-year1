// TD3:EX4 Ecrire un programme qui demande un nombre compris entre 10 et 20, jusqu’à ce que la réponse convienne. En cas de réponse supérieure à 20, on fera apparaître un message : « Plus grand !», et inversement, « Plus petit ! » si le nombre est inférieur à 10.

#include <stdio.h>
#include <stdlib.h>

int main(){
    int n;
    printf("Entrer un nombre\n");
    scanf("%d",&n);
    while(n<10 || n>20){
      if(n<10){
        printf("Plus petit!\n");
      }
      if(n>20){
        printf("Plus grand!\n");
        
      }  
      printf("Entrer un nombre\n");
        scanf("%d",&n);
    }
    
    return 0;
}