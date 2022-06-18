import numpy as np
from erdoRandom import erdosRenyi
from barabasRandom import barabasi_albert
from algorithmFloyd import floyd_warshall
from grafoGrade import grafoGrade
from plotGraph import plotGraph
import matplotlib.pyplot as plt

print("Escolha3 o modelo base para gerar o grafo:")
tipo = int(input("\n1 -  Erdos-Renyi \n2 - Barabasi-Albert \n3 - Grafo grade\n\n"))

if(tipo == 1):
    node = int(input("Insira a quantidade de vértices do grafo:"))
    prob = float(input("Insira a probabilidade de conexão das arestas:"))
    G = erdosRenyi(node, prob)
    floyd_warshall(G)
elif(tipo == 2):
    node = int(input("Insira a quantidade de vértices do grafo:"))
    edge = int(input(
        "Insira número de arestas a serem anexadas de um novo nó a nós existentes do grafo:"))
    G = barabasi_albert(node, edge)
    floyd_warshall(G)
elif(tipo == 3):
    scale = int(input("Insira a escala do seu grafo grade:"))
    G = grafoGrade(scale)
    floyd_warshall(G)
else:
    print("Opção inválida")

plt.show()