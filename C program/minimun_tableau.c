#include <stdio.h>
#include <stdlib.h>

int main(){
    int list_numbers[10],imin;
    imin=0;
    for(int i=0;i<10;i++){
        printf("Enter a number\n");
        scanf("%d",&list_numbers[i]);
             
        if(list_numbers[i]<list_numbers[imin]){
            imin=i;
        }
    }
    printf("L'indice du min est %d",imin+1);
    return 0;
}