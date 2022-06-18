import random
import numpy as np
import matplotlib.pyplot as plt
from plotGraph import plotGraph, plotMatrix


class NodeGrid:
    def __init__(self, index, l, c, n):
        def calcVizinhos(i, j, n):
            linha = coluna = []

            if i == 0:
                linha = [i, i+1]
            elif i == n-1:
                linha = [i-1, i]
            else:
                linha = [i-1, i, i+1]

            if j == 0:
                coluna = [j, j+1]
            elif j == n-1:
                coluna = [j-1, j]
            else:
                coluna = [j-1, j, j+1]

            return [(a*n)+b+1 for a in linha for b in coluna if(i != a or j != b)]
        self.index = index
        self.vizinhos = calcVizinhos(l, c, n)



def grafoGrade(n):
    nodes = [NodeGrid((i*n)+j+1,i,j,n) for i in range(n) for j in range(n)]
    edges = [(node.index,edge) for node in nodes for edge in node.vizinhos]

    # Matriz Adjacência
    G = [[0 for i in nodes] for j in nodes]
    for edge in edges:
        G[edge[0]-1][edge[1]-1] = G[edge[1]-1][edge[0]-1] = 1
    plotMatrix("Matriz Adjacência",G)

    # Matriz de Custo 
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] != 0:
                G[i][j] = G[j][i] = random.randint(1, 10)
            else:
                if i != j:
                    G[i][j] = float('inf')
    plotMatrix("Matriz Custo",G)
    plotGraph(G)
    return np.array(G)

# print(NodeGrid)
