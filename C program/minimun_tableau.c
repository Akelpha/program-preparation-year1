#include <stdio.h>
#include <stdlib.h>

int main(){
    int list_numbers[10],imin,n;
    for(int i=0;i<=10;i++){
        printf("Enter a number\n");
        scanf("%d",&list_numbers[i]);
        //Enlever le n , initialisez le imin a 0 puis dans la condition mettre imin = i 
        n=i;
        imin=i+1;
        if(list_numbers[n]<=list_numbers[imin]){
            imin=n;
        }
    }
    printf("L'indice du min est %d",imin);
    return 0;
}