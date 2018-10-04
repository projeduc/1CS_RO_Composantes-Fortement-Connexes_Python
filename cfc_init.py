#!/usr/bin/env python
# -*- coding: utf-8 -*-

# list des composantes fortement connexes
composants = []
# ensemble des noeuds marqués plus
plus = set()
# ensemble des noeuds marqués moins
moins = set()
# ensemble des noeuds qui ne sont pas encore affectés à une composante
noeuds_restants = set()

# marquer les successeurs avec +
def marquer_successeurs(v, graph):
    global plus, noeuds_restants
    succ = graph[v] # récupérer la list des successeurs de ce noeud
    for u in succ: # parcourir les successeurs de v
        if u in noeuds_restants and not u in plus: # si un successeur u n'est pas marqué +
            plus.add(u) #marquer u avec +
            marquer_successeurs(u, graph) # marquer les successeurs de u avec +

# marquer les predecesseurs avec -
def marquer_predecesseurs(v, graph):
    global moins, noeuds_restants
    for u in graph: #parcourir les éléments u du graph
        if u in noeuds_restants:
            succ = graph[u] #récupérer les successeurs de chaque élément
            if (v in succ) and (u not in moins): # si v est un successeur de u et u n'est pas marqué -
                moins.add(u) # marquer u avec -
                marquer_predecesseurs(u, graph) # marquer les predecesseurs de u avec -

def composantes_connexes(graph):
    #Global: c'est pour accéder aux variables globales
    #Python considère tous qui est dans une fonction comme variable locale
    global composants, plus, moins, noeuds_restants
    # initialiser les listes
    composants = []
    plus = set()
    moins = set()
    # récupérer les noeuds à partir du graph
    noeuds_restants = set(graph.keys())

    while len(noeuds_restants) > 0 : # s'il existe des noeads restants (non affectés)
        v = list(noeuds_restants)[0] # récupérer un des noeuds restants
        plus.add(v) # marquer v avec +
        moins.add(v) # marquer v avec -
        marquer_successeurs(v, graph) # marqer ses successeurs avec +
        marquer_predecesseurs(v, graph) #marquer ses predecesseurs avec -
        inter = plus & moins # ensemble des noeuds marqués + et -
        composants.append(list(inter)) # ajouter cet ensemble comme  composante connexe
        noeuds_restants =  noeuds_restants - inter # supprimer ses éléments de la liste des noeuds restants
        plus = set() # vider la list des +
        moins = set() # vider la list des -

    return composants # retourner les composantes connexes
