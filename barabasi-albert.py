import random
import networkx as nx

def barabasi_albert():
    INF = float('inf')
    n = int(input("Digite a quantidade de VÉRTICES: "))
    p = int(input("Digite a quantidade de ARESTAS: "))
    G= nx.barabasi_albert_graph(n,p)
    
    lines = []
    for line in nx.generate_adjlist(G):
        lines.append(line)
        
    y = nx.parse_adjlist(lines, nodetype = int)
    quantVertice = len(y.nodes())
    lista_adjacencia = nx.to_numpy_array(y)
    
    for i in range(quantVertice):
        for j in range(quantVertice):
            if lista_adjacencia[i][j] == 0:
                lista_adjacencia[i][j] = INF
            else:
                lista_adjacencia[i][j] = random.randint(1, 10)
                
    return lista_adjacencia, quantVertice