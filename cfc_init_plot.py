#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cfc.initial import composantes_connexes
from manip.graphe_lire import lire
from manip.graphe_ecrire import sauvegarder, sauvegarder_cfc

graph = lire("graphs/g1.txt")

composantes = composantes_connexes(graph)

print ("Le graphe: ")
print(graph)
print ("Les composantes fortement connexes: ")
print(composantes)

sauvegarder(graph, "output/initial_g1_gr")
sauvegarder_cfc(graph, composantes, "output/initial_g1_cfc")
