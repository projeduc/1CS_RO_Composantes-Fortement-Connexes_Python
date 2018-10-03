#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cfc import composantes_connexes

graph = {
    1:[2], # 1 --> 2
    2:[1,5], # 2 --> 1, 2 --> 5
    3:[4], # 3 --> 4
    4:[3,5], # 4 --> 3, 4 --> 5
    5:[6], # 5 --> 6
    6:[7], # 6 --> 7
    7:[8], # 7 --> 8
    8:[6,9], # 8 --> 6, 8 --> 9
    9:[] # 9 n'a pas de successeurs
}

composantes = composantes_connexes(graph)

print(composantes)
