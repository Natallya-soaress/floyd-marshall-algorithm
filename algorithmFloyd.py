def floyd_warshall(G):
    distance = G

    for k in range(len(distance)):
        for i in range(len(distance)):
            for j in range(len(distance)):
                distance[i][j] = min(
                    distance[i][j], distance[i][k] + distance[k][j])
    return distance