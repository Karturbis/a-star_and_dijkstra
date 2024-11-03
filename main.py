import networkx as nx
import matplotlib.pyplot as plt
from real_map import generate_map_graph
from dijkstra import dijkstra
from a_star import a_star
from a_star import geopy_dis
from a_star import flatearther_dis


def main(G, pos, algorithm, start_node, end_node):
    if algorithm == "a_star":
        algorithm = a_star
    else:
        algorithm = dijkstra
    path_length, path = algorithm(G, pos, start_node, end_node, geopy_dis)
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
    nx.draw(G, pos, with_labels=False, node_size=0)
    nx.draw_networkx_edges(G, pos, G.edges(), edge_color='k')
    #nx.draw_networkx_edge_labels(
    #G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)}
#)
    nx.draw_networkx_edges(G, pos, edges, edge_color='r')
    print("draw will start now in main.py")
    plt.show()




if __name__ == "__main__":
    G, pos = generate_map_graph()
    main(G, pos, a_star, 1770439267, 11201847066,)
