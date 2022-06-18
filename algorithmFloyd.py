import numpy as np

from plotGraph import plotMatrix


def floyd_warshall(M):
    g = M
    for k in range(len(g)):
        for i in range(len(g)):
            for j in range(len(g)):
                g[i][j] = min(
                    g[i][j], g[i][k] + g[k][j])
    plotMatrix("Matriz Custo Mínimo",M)
