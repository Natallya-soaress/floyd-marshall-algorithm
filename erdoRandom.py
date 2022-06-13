import random
import numpy as np

class Vertice:
    def __init__(self, index):
        self.index = index
        self.vizinhos = []


def erdosRenyi(n, p):
    vertice = [Vertice(i) for i in range(n)]
    aresta = [(i, j) for i in range(n)
              for j in range(i) if (random.random() < p)]
    values = [random.randint(0, 9) for i in aresta]

    def valueAresta(i: Vertice, j: Vertice):
        value = float("inf")
        for it in aresta:
            if(it == (i.index, j.index)):
                value = values[aresta.index((i.index, j.index))]
            if(it == (j.index, i.index)):
                value = values[aresta.index((j.index, i.index))]
            if(i.index == j.index):
                value = 0
        return value

    G = [[valueAresta(i, j) for j in vertice] for i in vertice]

    return np.array(G)


