import networkx as nx
import matplotlib.pyplot as plt
from real_map import generate_map_graph
from dijkstra import dijkstra
from a_star import a_star
from a_star import distance


def main(algorithm, start_node, end_node):
    G, pos = generate_map_graph()
    path_length, path = algorithm(G, start_node, end_node, distance, pos)
    edges = []
    path_string_printable = f"{start_node}"
    for i, node in enumerate(path):
        try:
            path_string_printable = f"{path_string_printable} -> {path[i+1]}"
            edges.append((node, path[i + 1]))
        except IndexError:
            pass
    print(f"The shortest path from {start_node} to {end_node} is: {path_string_printable}")
    print(f"Pathlength is: {path_length}")
    colors = nx.get_edge_attributes(G, "color").values()
    nx.draw(G, pos, with_labels=False, node_size=0)
    nx.draw_networkx_edges(G, pos, G.edges(), edge_color='k')
    #nx.draw_networkx_edge_labels(
    #G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)}
#)
    nx.draw_networkx_edges(G, pos, edges, edge_color='r')
    print("draw will start now in main.py")
    plt.show()




if __name__ == "__main__":
    main(a_star, 1770439267, 11201847066)