#!/usr/bin/env python
# -*- coding: utf-8 -*-

from graphviz import Digraph

# Une liste des couleurs
colors = ["green", "blue", "red", "yellow", "magenta", "pink", "violet", "cyan"]

# Sauvegarder un graphe formaté comme une liste d'adjacence dans un fichier PNG "nom_fichier"
def sauvegarder(graphe, nom_fichier):
    g = Digraph(format='png')
    for v in graphe: # boucler sur les clés du tableau associatif (les noeuds)
        g.node(str(v)) # créer un noeud
        for u in graphe[v]: # boucler sur les éléments d'une liste repésentant les successeurs de v
            g.node(str(u)) # créer un noeud
            g.edge(str(v), str(u)) # créer un arc
    g.edge_attr.update(arrowhead='vee') # formater les flèches sous forme V
    g.render(nom_fichier, view=True) # écrire le fichier

# Sauvegarder un graphe formaté comme une liste d'adjacence dans un fichier PNG "nom_fichier"
# en donnant une liste des listes représentant la liste des CFC
def sauvegarder_cfc(graphe, liste_cfc, nom_fichier):
    g = Digraph(format='png')
    for idx, cfc in enumerate(liste_cfc): # boucler sur les CFCs
        g.attr('node', style='filled', color=colors[idx]) # pour chaque CFC  attribuer une couleur
        for v in cfc: # boucler sur les noeuds formants une CFC
            g.node(str(v)) # créer un noeud

    for v in graphe: # boucler sur les noeud du ggraphe
        for u in graphe[v]: # boucler sur les successeurs de chaque noeud
            g.edge(str(v), str(u)) # créer un arc
    g.edge_attr.update(arrowhead='vee') # formater les flèches sous forme V
    g.render(nom_fichier, view=True) # écrire le fichier
