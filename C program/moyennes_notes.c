#include <stdio.h>
#include <stdlib.h>

int main(){
    int notes_tab[20],sum,CSN;
    float moy;

    sum=0; 
    CSN =0;
    for(int i=0;i<20;i++){
        printf("Enter a student's notes.\n");
        scanf("%d",&notes_tab[i]);
        sum = sum+notes_tab[i];
    }
    moy= sum/20;
    for(int l =0;l<20;l++){
        if(notes_tab[l]> moy){
            CSN++;
        }
    }
    printf("La moyenne et le nombre de notes superieurs a la moyenne sont %2.f et %d",moy,CSN);
    return 0;
}