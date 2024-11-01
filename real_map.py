import json
from geopy.distance import distance
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from pansi import ansi

FALLBACK_MAP_FILE = "test_map_data/test_02.geojson"

def generate_map_graph(map_file: str=None):
    if not map_file:
        map_file = FALLBACK_MAP_FILE
    with open(map_file) as map_data_raw:
        map_data = json.load(map_data_raw)
    map_data_nodes = {}
    map_data_edges = {}
    for element in map_data["elements"]:
        if element["type"] == "node":
            map_data_nodes[element["id"]] = (element["lon"], element["lat"])
        elif element["type"] == "way":
            map_data_edges[element["id"]] = element["nodes"]

    G = nx.Graph()
    pos = {}
    nodes = []

    for node, position in map_data_nodes.items():
        nodes.append(node)
        pos[node] = np.array([position[0], position[1]])


    for key, edge in map_data_edges.items():
        for i, start_node in enumerate(edge):
            try:
                G.add_edge(
                    start_node,
                    edge[i + 1],
                    length=distance(
                        map_data_nodes[start_node], map_data_nodes[edge[i + 1]]
                    ),
                )
            except IndexError:
                continue

    G.add_nodes_from(nodes)
    print(
        "Graph is connected"
        if nx.is_connected(G)
        else f"{ansi.red}Warning: Graph is not connected{ansi.reset}"
    )
    return (G, pos)


if __name__ == "__main__":
    map_file = "test_map_data/test_02.geojson"
    G, pos = generate_map_graph(map_file)
    nx.draw(G, pos, node_size=1)
    plt.show()