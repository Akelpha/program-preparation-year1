/*TD2:Ex7Ecrire un programme en C permettant de saisir le prix unitaire et la quantité commandée d'un
article. Le programme affichera le prix à payer, le port, et la remise sachant que :
- le port est gratuit si le montant hors taxe est supérieur à 1000 dhs
- le port est 3% dans le cas contraire
- la remise est de 5% si le montant hors taxe est compris entre 300 et 1000 dhs et de 10% au-delà
de 1000 dhs.*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    // PP for the port's price
    int unit_price, quantity;
    float discount, MHT, PP, total;

    printf("Enter your unit_price and the quantity of this article.\n");
    scanf("%d %d", &unit_price, &quantity);
    MHT = unit_price * quantity;
    
    // Compute the port
    if (MHT > 1000)
    {
        PP = 0;
    }
    else
    {
        PP = MHT * 0.03;
    }
    // Compute the discount
    if (MHT >= 300 && MHT <= 1000)
    {
        discount = MHT * 0.05;
    }
    else if (MHT > 1000)
    {
        discount = MHT * 0.10;
    }
    else{
        discount = 0;
    }
    total = MHT + PP - discount;
    printf("The MHT is %.2f,the total_price is %.2f ,your PP is %.2f and the discount is %.2f.\n", MHT, total,PP, discount);
    return 0;
}