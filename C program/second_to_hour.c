#include <stdio.h>
#include <stdlib.h>

int main(){
    int T,seconde,minute,heure;
    printf ("Enter the time in seconds: \n");
    scanf ("%d", &T);
    heure = T/3600;
    minute = (T % 3600) / 60;
    seconde = (T % 3600) % 60;
    printf("Your time T in hour,minute and second is %dh: %dm : %ds. \n",heure,minute,seconde);
    return 0;
}