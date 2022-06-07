import random
import matplotlib.pyplot as plt
import networkx as nx

def create_network(n:int, p:float):
    """ Creates a graphical representation of an Erdos-Renyi network

        Parameters: 
        -n: number of nodes of the network.
        -p: probability that each pair of nodes will be connected.

        Returns:
        An graph representing an Erdos-Renyi network with the given n and p.
    """
    "creating empty graph"
    G = nx.Graph()

    "adding nodes"
    G.add_nodes_from(range(1, n+1))

    "adding edges randomly based on probability p"
    for i in G.nodes():
        for j in G.nodes():
            if i < j:
                temp_prob = random.random()
                if temp_prob < p:
                    G.add_edge(i,j)

    return G

def avg_degree(G):
    """ Calculates the average degree of the given graph.

        Parameters: 
        -G: the graph in the form of a networkx graph.

        Returns:
        Average degree of the graph.
    """
    sum_degrees = 0
    num_nodes = len(G.nodes())

    for nodes in G.nodes():
        deg = G.degree[nodes]
        sum_degrees += deg

    avg_degree = sum_degrees/num_nodes

    return avg_degree

def avg_pathlen(G):
    """ Calculates the average path length of the given graph.

        Parameters: 
        -G: the graph in the form of a networkx graph.

        Returns:
        Average path length of the graph.
    """
    return nx.average_shortest_path_length(G,False)

def avg_clustering_coefficient(G):
    """ Calculates the average clustering coefficient of each node of the given graph.

        Parameters: 
        -G: the graph whose average degree is being calculates.

        Returns:
        Average clustering coefficient of the graph
    """
    total_clustering = 0
    for node in G.nodes():
        total_clustering += nx.clustering(G, node)
    avg = total_clustering/len(G.nodes())

    return avg

def plot_deg_distribution(G):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees)
    plt.xlabel('k')
    plt.ylabel('p(k)')
    plt.show()

def main(n_inp:int, p_inp:float):
    """ main function to call functions and handle each configuration of the network, where each
        configuration will be run 30 times.

        Parameters:
        n_inp: number of nodes of network given by us
        p_inp: probabiliy of pair of nodes linking given by us

        Returns: 
        None
    """ 
    avg_avg_deg = 0
    avg_avg_pathlen = 0
    avg_avg_clust = 0

    for i in range(10):
        g = create_network(n_inp, p_inp)
        avg_avg_deg += avg_degree(g)
        avg_avg_pathlen += avg_pathlen(g)
        avg_avg_clust += avg_clustering_coefficient(g)

    avg_avg_pathlen = round(avg_avg_pathlen/10,4)
    avg_avg_deg = round(avg_avg_deg/10,4)
    avg_avg_clust = round(avg_avg_clust/10,4)

    print(
        "Average Estimates for configuration n =",n_inp,"p=",p_inp,
          ":\n Average Degree:",avg_avg_deg,
          "\n Average Path length:",avg_avg_pathlen,
          "\n Average Clustering Coefficient:",avg_avg_clust
         )

    plot_deg_distribution(create_network(n_inp , p_inp))

main(100, 0.10)