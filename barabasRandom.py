import random
import networkx as nx

def barabasi_albert(n, m):
    INF = float('inf')
    G = nx.barabasi_albert_graph(n, m)
    lista_adjacencia = nx.to_numpy_array(G)

    for i in range(n):
        for j in range(n):
            if lista_adjacencia[i][j] == 0:
                if i != j:
                    lista_adjacencia[i][j] = INF
            else:
                lista_adjacencia[i][j] = lista_adjacencia[j][i] = int(
                    random.randint(1, 10))
    return lista_adjacencia
