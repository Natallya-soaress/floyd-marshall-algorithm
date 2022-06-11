import networkx as nx
import random

class Vertice:
       def _init_(self, index):
            self.index = index
            self.vizinhos = []
 
def _repr_(self):
      return repr(self.index)

def erdosRenyi(n,p): 
   #limpar()
   vertice = [Vertice(i) for i in range(n)]
   aresta = [(i,j) for i in range(n) for j in range(i) if random.random() < p]
 
 
   for (i,j) in aresta:
      vertice[i].vizinhos.append(vertice[j])
      vertice[j].vizinhos.append(vertice[i])
 
   return vertice,aresta