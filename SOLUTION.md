Le code de eulerian.py fonctionne avec les fichiers hard_to_choose.txt et islands.txt, mais pas avec paris_map.txt.
L'optimisation du code peut donc se faire sur plusieurs points, dont le choix de l'algorithme :

L'algorithme de Fleury est simple, mais il peut être amélioré pour être plus rapide sur des graphes de grande taille, comme celui de paris_map.txt. Une approche alternative consiste à utiliser l'algorithme de Hierholzer, basé sur la recherche d'un cycle eulérien, qui peut être plus efficace dans la plupart des cas.


Exécution du code :
Pour exécuter le code du fichier eulerian.py, il faut passer en ligne de commande : python eulerian.py nom_du_fichier.txt
Avec nom_du_fichier.txt étant : hard_to_choose.txt, islands.txt ou encore paris_map.txt