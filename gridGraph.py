import random
import numpy as np
from plotService import plot_graph, plot_matrix

class NodeGrid:
    def __init__(self, index, l, c, n):
        def getNeighbors(l, c, n):
            def neighbors_for_axes(axe):
                if axe == 0:
                    arrayAxe = [axe, axe+1]
                elif axe == n-1:
                    arrayAxe = [axe-1, axe]
                else:
                    arrayAxe = [axe-1, axe, axe+1]
                return arrayAxe      
            line = neighbors_for_axes(l)
            column = neighbors_for_axes(c)
            return [(i*n)+j+1 for i in line for j in column if(l != i or c != j)]
        self.index = index
        self.vizinhos = getNeighbors(l, c, n)


def get_grid_graph(n):
    nodes = [NodeGrid((i*n)+j+1,i,j,n) for i in range(n) for j in range(n)]
    edges = [(node.index,edge) for node in nodes for edge in node.vizinhos]

    # Matriz Adjacência
    G = [[0 for i in nodes] for j in nodes]
    for edge in edges:
        G[edge[0]-1][edge[1]-1] = G[edge[1]-1][edge[0]-1] = 1
    plot_matrix("Matriz Adjacência",G)

    # Matriz de Custo 
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] != 0:
                G[i][j] = G[j][i] = random.randint(1, 10)
            else:
                if i != j:
                    G[i][j] = float('inf')
    plot_matrix("Matriz Custo",G)
    plot_graph(G)
    return np.array(G)
