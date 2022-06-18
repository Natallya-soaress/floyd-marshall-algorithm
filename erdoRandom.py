import random
import numpy as np

from plotGraph import plotGraph, plotMatrix


def erdosRenyi(n, p):
    nodes = [i for i in range(n)]
    edges = [(i, j) for i in range(n) for j in range(i) if (random.random() < p)]

    # Matriz Adjacência
    G = [[0 for i in nodes] for j in nodes]
    for edge in edges:
        G[edge[0]-1][edge[1]-1] = G[edge[1]-1][edge[0]-1] = 1
    plotMatrix("Matriz Adjacência",G)

    # Matriz de Custo 
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                G[i][j] = G[j][i] = random.randint(1, 10)
            else:
                if i != j:
                    G[i][j] = float('inf')
    plotMatrix("Matriz Custo",G)
    plotGraph(G)


    return np.array(G)


