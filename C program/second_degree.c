//TD2:Ex2 Écrire un programme qui calcule et affiche les solutions d'une équation du second degré de la forme ax2+ bx+c=0.

#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main (){
    int a,b,c;
    float d,x1,x2;
    printf("Enter your 3 numbers for your second degree equation like ax^2+ bx+c=0\n");
    scanf("%d %d %d",&a,&b,&c);
    d = pow(b,2)- 4*a*c;
    if(d>0){
       x1= (-b+sqrt(d))/2*a;
       x2= (-b-sqrt(d))/2*a;
       printf("the solution of your equation is %.2f for X1 and %.2f for X2.\n",x1,x2);
    }else if(d==0){
        x1=-b/2*a;
        x1=x2;
        printf("the solution of your equation is %.2f for X1 and %.2f for X2(there are egal).\n",x1,x2);
    }else{
        printf("the solution is not real.\n");
    }
    return 0;
}