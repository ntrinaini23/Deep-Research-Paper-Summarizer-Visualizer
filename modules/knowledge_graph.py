import networkx as nx
import matplotlib.pyplot as plt

def build_knowledge_graph(concepts, relationships):
    G = nx.Graph()
    for concept in concepts:
        G.add_node(concept)
    for a, b in relationships:
        G.add_edge(a, b)

    plt.figure(figsize=(8,8))
    nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray", node_size=2000, font_size=10)
    plt.savefig("outputs/graphs/knowledge_graph.png")
    plt.close()
