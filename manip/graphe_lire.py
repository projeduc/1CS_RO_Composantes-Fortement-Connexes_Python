#!/usr/bin/env python
# -*- coding: utf-8 -*-

# créer une liste assosiative représentant le graphe à partir d'un fichier
def lire(nom_fichier):
    g = {}
    with open(nom_fichier, "r") as f:
        for line in f:
            [k, v] = line.split(":")
            succ = map(str.strip, v.split(","))
            for s in succ:
                if s not in g:
                    g[s] = []
            g[k] = succ

    return g
