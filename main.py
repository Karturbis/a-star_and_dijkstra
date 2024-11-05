import networkx as nx  # used to implement the graph
import matplotlib.pyplot as plt  # used to plot the graph
from real_map import generate_map_graph  # used to generate graph of a real map
from dijkstra import dijkstra  # find shortest path with Dijkstras algorithm
from a_star import a_star  # find shortest path with A* algorithm
from a_star import geopy_dis  # used to get the georaphical distances in the graph
from a_star import flatearther_dis  # used to get euclidean distances in the graph


def main(G, pos, algorithm, start_node, end_node, heuristic=flatearther_dis):
    """Displays the given Graph, with the edges from start_node to end_node
    in red color.
    Uses @algorithm to find the shortest path.
    If A* is used:
    heuristic can be set to flatearther_dis, to claculate the distance, assuming
    the Earth is flat (used in geographical small graphs) or geopy_dis, to calculate
    the distance on an earth ellipsoid (using WGS-84). Only use geopy_dis, if the
    graph @G is a graph of a map with geographical valid positions on the nodes."""
    if algorithm == "a_star":
        algorithm = a_star
    else:
        algorithm = dijkstra
    # calling the given algorithm:
    path_length, path = algorithm(G, pos, start_node, end_node, heuristic)
    edges = []
    # make a printable string from  the algorithm output
    path_string_printable = f"{start_node}"
    for i, node in enumerate(path):
        try:
            path_string_printable = f"{path_string_printable} -> {path[i+1]}"
            edges.append(
                (node, path[i + 1])
            )  # append all edges of the path to var edges
        except IndexError:
            pass
    print(
        f"The shortest path from {start_node} to {end_node} is: {path_string_printable}"
    )
    print(f"Pathlength is: {path_length}")
    nx.draw(G, pos, with_labels=False, node_size=0)  # make the graph drawable
    nx.draw_networkx_edges(
        G, pos, G.edges() - edges, edge_color="k"
    )  # make non path edges in black
    nx.draw_networkx_edges(
        G, pos, edges, edge_color="r"
    )  # make all edges of the path red
    plt.show()  # open a window and draw the graph in it


if __name__ == "__main__":
    G, pos = generate_map_graph()  # generate a map, using real_map.py
    main(
        G,
        pos,
        a_star,
        3428385949,  # position of the teachers parking lot
        3428399062,  # position of the rewe
        flatearther_dis,  # using flatearther dis, because distances in G are small
    )
