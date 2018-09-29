# Composantes Fortement Connexes

Etant donnée un graph orienté G(V, A), où V est l'ensemble des noeuds et A est l'ensemble des arcs, on dit qu'un graph partiel G'(V',A') de G forme une composante fortement connexe si et seulement si quelque soit deux noeuds u, v de V' il existe un chemin de u vers v.

## Quelques applications

* Identifier des relations fortes entre les groupes sur les réseaux sociaux.
* La base de plusieurs techniques de vérification de systèmes ([2-SAT](https://fr.wikipedia.org/wiki/Problème_2-SAT), [Model-Checking](https://fr.wikipedia.org/wiki/Vérification_de_modèles)...)

## Algorithme initial
Cet algorithm nécessite plusieurs itérations sur un graph de N noeuds afin de trouver les composantes fortement connexes (CFC).

Dans un graph G(V, A) où V est l'ensemble des nœuds et A est l'ensemble des arcs, on définit les fonctions suivantes:
* __marquer_prédécesseurs(v)__: marquer récursivement les prédécesseurs d'un nœud, jusqu'à ce qu'il n'y a plus à marquer
* __marquer_successeurs(v)__: marquer récursivement les successeurs d'un nœud, jusqu'à ce qu'il n'y a plus à marquer

On définit aussi quelques variables:
* __P__: l'ensemble des noeuds marqués (+) (remplis par la fonction marquer_successeurs)
* __M__: l'ensemble des noeuds marqués (-) (remplis par la fonction marquer_prédécesseurs
* __R__: l'ensemble des noeuds restants (qui ne sont pas encore affectés à une composante connexe)
* __S__: l'ensemble des composantes fortement connexes; c'est un ensemble des ensembles des neouds.
* __C__: l'ensemble des noeuds formants une composante fortement connexe

```
ALGORITHME cfc-initial
ENTREES: G(V, A)
SORTIE: S
VARIABLES GLOBALES:
        S = ∅ //L'ensemble des CFC
        R = V //L'ensemble des noeuds restants
        P = ∅ //L'ensemble des noeuds marqués +
        M = ∅ //L'ensemble des noeuds marqués -

PROCEDURE marquer_prédécesseurs(v)
   POUR CHAQUE (u, v) ∈ A FAIRE
      SI u ∉ M FAIRE  
         M = M ∪ {u}
         marquer_prédécesseurs(u)
      FIN SI
   FIN POUR
FIN PROCEDURE

PROCEDURE marquer_successeurs(v)
   POUR CHAQUE (v, u) ∈ A FAIRE
      SI u ∉ P FAIRE  
         P = P ∪ {u}
         marquer_successeurs(u)
      FIN SI
   FIN POUR
FIN PROCEDURE

DEBUT
   POUR CHAQUE v ∈ R FAIRE
      P = {v}
      M = {v}
      marquer_prédécesseurs(v)
      marquer_successeurs(v)
      C =  P ∩ M //Les noeuds marqués + et -
      R = R - C
   FIN POUR
FIN
```

## Algorithme de Kosaraju

Liens:
* Sur [Wikipedia](https://fr.wikipedia.org/wiki/Algorithme_de_Kosaraju)
* Sur [geeksforgeeks](https://www.geeksforgeeks.org/strongly-connected-components/) avec un code en C++, Java et Python.
* [Une implémentation en Python](https://github.com/ladamalina/coursera-algo/blob/master/PQ4.%20SCCs/kosaraju.py)
* [Une autre en Python](https://github.com/TheAlgorithms/Python/blob/master/Graphs/scc_kosaraju.py)
* [Une autre en Python](https://gist.github.com/JeremieGomez/74de2d3e1268c48e63a3)

## Algorithme de Tarjan

Liens:
* Sur [Wikipedia](https://fr.wikipedia.org/wiki/Algorithme_de_Tarjan)
* [Une implémentation en Python](https://github.com/bwesterb/py-tarjan/)
* [Une autre en Python](https://github.com/TheAlgorithms/Python/blob/master/Graphs/tarjans_scc.py)

```
ALGORITHME cfc-tarjan
ENTREES: G(V, A)
SORTIE: S
VARIAB
S = ∅ //L'ensemble des CFC
R = V //L'ensemble des noeuds restants
i = 1 //L'index de la composante
POUR CHAQUE v ∈ R FAIRE
   P = ∅ //L'ensemble des noeuds marqués +
   M = ∅ //L'ensemble des noeuds marqués -
   marquer_prédécesseurs(v)
   marquer_successeurs(v)
   C =  P ∩ M //Les noeuds marqués + et -
   marquer_composante(C, i)
   i = i + 1
   R = R - C
FIN POUR
```
