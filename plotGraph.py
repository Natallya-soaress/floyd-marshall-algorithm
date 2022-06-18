import networkx as nx
import matplotlib.pyplot as plt


def plotGraph(M):
    G = nx.Graph()
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] != float("inf") and M[i][j] != 0:
                G.add_edge(i, j, weight=M[i][j])
    pos = nx.spring_layout(G)
    newFigure()
    nx.draw(G, pos, with_labels=True, width=1, linewidths=1,
            node_size=500, node_color='pink', alpha=0.9)
    labels = {(u,v): c["weight"] for (u,v,c) in G.edges.data()}
    nx.draw_networkx_edge_labels(G,pos,font_color='red',edge_labels=labels)

def plotMatrix(name, G):
    newFigure()
    plt.title(name)
    plt.axis("off")
    iColors = ["#A4B0F5"] * len(G)
    plt.table(cellText=G, colLabels=(range(len(G))),
              rowLabels=(range(len(G))), loc='center', rowColours=iColors, colColours=iColors)


def newFigure():
    fig = 0
    while (plt.fignum_exists(fig)):
        fig = fig+1
    plt.figure(fig)
    return fig
