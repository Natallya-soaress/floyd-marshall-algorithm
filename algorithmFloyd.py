import numpy as np

def floyd_warshall(G):
    for k in range(len(G)):
        for i in range(len(G)):
            for j in range(len(G)):
                G[i][j] = min(
                    G[i][j], G[i][k] + G[k][j])
    print("\nMatriz Custo Mínimo")
    print(np.array(G))
    return G