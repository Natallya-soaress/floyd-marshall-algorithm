from erdoRandom import erdosRenyi
from barabasRandom import barabasi_albert
from algorithmFloyd import floyd_warshall



print("Barabasi Albert\n")
Gbar = barabasi_albert(5, 1)
print("Grafo Aleatório\n", Gbar)
floyd_warshall(Gbar)
print("\n\nCaminho mínimo\n", Gbar)

print("\n\n\nErdo Renyi\n")
Gbar = erdosRenyi(5, 0.5)
print("Grafo Aleatório\n", Gbar)
floyd_warshall(Gbar)
print("\n\nCaminho mínimo\n", Gbar)


