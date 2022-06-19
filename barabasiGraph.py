import random
import networkx as nx
from plotService import plot_graph, plot_matrix

def get_barabasi_albert(n, m):
    G = nx.barabasi_albert_graph(n, m)

    # Matriz Adjacência
    G = nx.to_numpy_array(G)
    plot_matrix("Matriz Adjacência",G)

    # Matriz de Custo 
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                G[i][j] = G[j][i] = random.randint(1, 10)
            else:
                if i != j:
                    G[i][j] = float('inf')
    plot_matrix("Matriz Custo",G)
    plot_graph(G)
    return G
