#include <stdio.h>
#include <stdlib.h>


int main(){
    int numbers[20],imax;

    imax= 0;
    for(int i=0;i< 20;i++){
        printf("Ecrire le nombre %d\n",i+1);
        scanf("%d",&numbers[i]);
    }
    for(int i=1;i<=20;i++){
        
        if(numbers[i] > numbers[imax]){
            imax = i;
        }
    }

    printf("Le plus grand de ces nombres est : %d \n",numbers[imax]);
    printf("It was the %d number \n",imax);
   return 0;
}