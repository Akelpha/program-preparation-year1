#include <stdio.h>
#include <stdlib.h>

int main(){
    int n,s;
    printf("Entrer un entier pair \n");
    scanf("%d",&n);
    for(int i= 2;i<=n;i=i+2){
        s=s+1;
    }
    printf("%d est divible %d fois par 2",n,s);
}


