import networkx as nx
import matplotlib.pyplot as plt


def __new_figure():
    fig = 1
    while (plt.fignum_exists(fig)): fig = fig+1 
    plt.figure(fig)
    return fig


def plot_graph(M):
    G = nx.Graph()
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] != float("inf") and M[i][j] != 0:
                G.add_edge(i, j, weight=M[i][j])
    __new_figure()
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, width=1, linewidths=1, node_size=500, node_color='pink', alpha=0.9)
    labels = {(u, v): c["weight"] for (u, v, c) in G.edges.data()}
    nx.draw_networkx_edge_labels(G, pos, font_color='red', edge_labels=labels)


def plot_matrix(name, G):
    __new_figure()
    plt.title(name)
    plt.axis("off")
    iColors = ["#A4B0F5"] * len(G)
    cellColors = [["#fff" for c in range(16)] for r in range(16)]
    for i in range(len(G)):
        for j in range(len(G)):
            if (G[i][j] > 0 and G[i][j] != float("inf")):
                cellColors[i][j] = "#B3D6C6"
    plt.table(cellText=G, colLabels=(range(len(G))),rowLabels=(range(len(G))), loc='center', rowColours=iColors, colColours=iColors, cellColours=cellColors)
