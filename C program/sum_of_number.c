// TD3:EX2 Écrire un programme qui demande à l’utilisateur de saisir un nombre entier strictement supérieur à 1, et qui calcule la somme des entiers jusqu’à ce nombre. Par exemple, si on entre 6, le programme doit calculer et afficher la somme de 1+2+3+4+5+6

#include <stdio.h>
#include <stdlib.h>

int main(){
 int n,sum;

 sum =0;

 do{
  printf("Enter a number above 1.\n");
  scanf("%d",&n);
  sum = (n*(n+1))/2;
 }
 while(n<1);
 printf("the sum is %d",sum);

 /*
 or
 int n,s;
 s=0;
 do{
 printf("Saisir n");
 scanf("%d",&n);
 }while(n<=1)

 for(int i=0;i<=n;i++){
   s=s+i;
 }
 printf("la somme est %d",s)
 
 */
 return 0;
}