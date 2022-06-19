from plotService import plot_matrix

def floyd_warshall(M):
    for k in range(len(M)):
        for i in range(len(M)):
            for j in range(len(M)):
                M[i][j] = min(
                   M[i][j],M[i][k] + M[k][j])
    plot_matrix("Matriz Custo Mínimo",M)
