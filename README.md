# Composantes Fortement Connexes

## Algorithm initial 
Cet algorithm nécessite plusieurs itérations sur un graph de N noeuds afin de trouver les composantes fortement connexes (CFC). 

Dans un graph G(V, A) où V est l'ensemble des nœuds et A est l'ensemble des arcs, on définit les fonctions suivantes:
* __marquer_prédécesseurs(v)__: marquer récursivement les prédécesseurs d'un nœud, jusqu'à ce qu'il n'y a plus à marquer
* __marquer_successeurs(v)__: marquer récursivement les successeurs d'un nœud, jusqu'à ce qu'il n'y a plus à marquer
* * __marquer_composante(c, i)__: marquer un ensemble de noeud comme composante avec un numéro donnée i
On définit aussi quelques ensembles:
* __plus__: l'ensemble des noeuds marqués (+) (remplis par la fonction marquer_successeurs)
* __moins__: l'ensemble des noeuds marqués (-) (remplis par la fonction marquer_prédécesseurs
* __restants__: l'ensemble des noeuds restants

```
restants = V
index = 1 //L'index de la composante
Tantque restants n'est pas vide faire
   v = un noeud de restants
   plus = {}
   moins = {}
   marquer_prédécesseurs(v)
   marquer_successeurs(v)
   
   composante =  plus &cap; moins 
   marquer_composante(composante, index)
   index = index + 1
   restants = restants - composante
Fin tantque
```
