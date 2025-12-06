#include <stdio.h>
#include <stdlib.h>

int main (){
    int number;
    printf("Enter a number \n");
    scanf("%d", &number);
    if(number > 0){
        printf("This number is positif. \n");
    }
    else if(number < 0){
        printf("This number is negatif. \n");
    }
    else{
        printf("This number is zero. \n");
    }

}