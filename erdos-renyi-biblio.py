import networkx as nx
import matplotlib.pyplot as plt
  
G= nx.erdos_renyi_graph(10 ,0.5)
nx.draw(G, with_labels=True)
plt.show()



