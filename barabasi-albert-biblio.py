import networkx as nx
import matplotlib.pyplot as plt

G= nx.barabasi_albert_graph(10, 5)
nx.draw(G, with_labels=True)
plt.show()