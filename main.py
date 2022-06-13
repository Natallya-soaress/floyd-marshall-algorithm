from erdoRandom import erdosRenyi
from barabasRandom import barabasi_albert
from algorithmFloyd import floyd_warshall
import networkx as nx

print("Insira o modelo base para gerar o grafo:")
tipo = int(input("\n1 -  Erdos-Renyi \n2 - Barabasi-Albert \n3 - Grafo grade"))

if(tipo == 1):
    vertice = int(input("Insira a quantidade de vértices do grafo:"))
    probabilidade = float(input("Insira a probabilidade de conexão das arestas:"))
    G = erdosRenyi(vertice, probabilidade)
    floyd_warshall(G)
    print(G)
    
elif(tipo == 2):
    vertice = int(input("Insira a quantidade de vértices do grafo:"))
    aresta = float(input("Insira a quantidade de arestas do grafo:"))
    G = barabasi_albert(vertice, aresta)
    floyd_warshall(G)
    print(G)
else:
    print("Opção inválida")



