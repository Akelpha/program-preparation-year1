#!/bin/bash 
if [ $# -eq 0 ];then
echo "Aucun parametre sur la ligne de commande"
else 
echo "Il y a $# parametre sur la ligne de commande"
for i in $*
do 
echo $i
donne
fi