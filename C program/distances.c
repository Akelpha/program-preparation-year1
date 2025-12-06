/*Écrire un programme qui calcule et affiche la distance entre deux points A et B du plan dont les coordonnées (XA , YA) et (XB , YB) sont entrées au clavier comme entiers.*/

#include <stdio.h> 
#include <stdlib.h>
#include <math.h>

int main (){
    int XA,YA,XB,YB,distance;
    printf("Please enter the coordinates of A and B\n");
    scanf("%d %d %d %d",&XA,&YA,&XB,&YB);
    distance = sqrt(pow((XB-XA),2)+pow((YB-YA),2));
    printf("The distance between A and B is %d",distance);
    return 0;
}