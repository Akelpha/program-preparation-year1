#!/bin/bash
echo "le contenu du repertoire courant est "
ls
echo "le contenu du repertoire donné comme parametre"
echo $1
echo 'donner le nom du repertoire"
read f
ls $f
