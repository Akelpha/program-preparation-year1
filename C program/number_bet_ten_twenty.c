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