#include <stdio.h>
#include <stdlib.h>

int main(){
    int N,t;
    t=0;
    printf("Enter a number\n");
    scanf("%d",&N);
    for(int i=0;i<=N;i+=2){
        printf("%d",i);
        t=t+1;
    }
    printf("Le nombre total de nombre pairs est %d",t);
    return 0;
}