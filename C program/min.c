// TD2:Ex1 Écrire un programme qui affiche le minimum de 3 entiers saisis au clavier.

#include <stdio.h>
#include <stdlib.h>

int main (){
    int a,b,c;
    printf("Enter 3 numbers\n");
    scanf("%d %d %d",&a,&b,&c);
    if(a<b && a<c){
        printf("The min of these 3 numbers is %d",a);
    }else if(b<a && b<c){
        //else if(B<C) c'est la meme chose
        printf("The min of these 3 numbers is %d",b);
    }else{
        printf("The min of these 3 numbers is %d",c);
    }
   return 0;
}
