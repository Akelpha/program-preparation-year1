#include <stdio.h>
#include <stdlib.h>

int main(){
    int diviseur[6];
    int k=0;
    for(int i=12;i>=1;i--){
        if(12 % i == 0){
          diviseur[k]=i;  
          k++;
        }
    }

    for (int l = 0; l < 6 ; l++) {       
         printf("%d \t", diviseur[l]);    
        }    

return 0;
}