from erdoGraph import get_erdos_renyi
from gridGraph import get_grid_graph
from barabasiGraph import get_barabasi_albert
from algorithmFloyd import floyd_warshall
import matplotlib.pyplot as plt

print("Escolha o modelo base para gerar o grafo:")
tipo = int(input("\n1 - Erdos-Renyi \n2 - Barabasi-Albert \n3 - Grafo grade\n\n"))

if(tipo == 1):
    node = int(input("Insira a quantidade de vértices do grafo:"))
    prob = float(input("Insira a probabilidade de conexão das arestas:"))
    G = get_erdos_renyi(node, prob)
elif(tipo == 2):
    node = int(input("Insira a quantidade de vértices do grafo:"))
    edge = int(input("Insira número de arestas a serem anexadas de um novo nó a nós existentes do grafo:"))
    G = get_barabasi_albert(node, edge)
elif(tipo == 3):
    scale = int(input("Insira a escala do seu grafo grade:"))
    G = get_grid_graph(scale)
else:
    print("Opção inválida")
    exit()
floyd_warshall(G)
plt.show()