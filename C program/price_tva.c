// TD1:Ex5 Écrire un programme en langage C qui lit le prix hors taxe (HT) d'un article, le nombre d'articles et le taux de TVA. Le programme calcule ensuite le prix total TTC et affiche le résultat.

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int article_numbers;
    float PHT, taxe_rate, MT, TTC;
    printf("Please enter the price excluding the taxe, the articles' numbers and the taxe rate\n");
    scanf("%f %d %f", &PHT, &article_numbers, &taxe_rate);
    MT = PHT * taxe_rate / 100;
    TTC = (PHT + MT) * article_numbers;
    printf("The total price with taxes included is %f\n", TTC);
    return 0;
}