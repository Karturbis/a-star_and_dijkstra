"""Generates a graph of a real map usong OSM
data (https://osm.org) compiled by overpass turbo
https://overpass-turbo.eu/s/1TBu"""
import json  # use json files
from geopy.distance import distance  # calculate the geographical distance
import networkx as nx  # used to implement the graph of the map
import numpy as np  # to use numpy arrays to update the position
import matplotlib.pyplot as plt  # used to draw the graph
from pansi import ansi  # used to make warnings red

FALLBACK_MAP_FILE = "test_map_data/test_02.geojson"

def generate_map_graph(map_file: str=None):
    """Gererates a graph from OSM data in overpass
    turbo xml format. The positions of the Nodes
    are their geo-coordinates, the edgelengths are
    real distances in km"""
    if not map_file:
        map_file = FALLBACK_MAP_FILE
    # put the map data into a Dict:
    with open(map_file, encoding="UTF-8") as map_data_raw:
        map_data = json.load(map_data_raw)
    map_data_nodes = {}
    map_data_ways = {}
    # put nodes and edges into the dicts:
    for element in map_data["elements"]:
        if element["type"] == "node":
            map_data_nodes[element["id"]] = (element["lon"], element["lat"])
        elif element["type"] == "way":
            map_data_ways[element["id"]] = element["nodes"]

    G = nx.Graph()  # Erstelle einen leeren Graphen.
    pos = {}
    nodes = []

    # update the position dict
    for node, position in map_data_nodes.items():
        nodes.append(node)
        pos[node] = np.array([position[0], position[1]])

    for _, edge in map_data_ways.items():
        for i, start_node in enumerate(edge):
            # Add all edges to the Graph, vertecies are added automatically, if edges
            # end or start in them:
            try:
                G.add_edge(
                    start_node,
                    edge[i + 1],  # Node, which is one step further, than the current node.
                    weight=float(str(distance(
                        map_data_nodes[start_node], map_data_nodes[edge[i + 1]]
                    ))[:-3]),  # Conversion to float and dropping of the "km" at the end of the string
                )
            except IndexError:  # Index Error occures, when the current edge is the last one in the way
                continue

    G.add_nodes_from(nodes)  # update the node positions
    # print warning if grap is not connected:
    print(
        "Graph is connected"
        if nx.is_connected(G)
        else f"{ansi.red}Warning: Graph is not connected{ansi.reset}"
    )
    return (G, pos)

if __name__ == "__main__":  # for tests
    map_file = "test_map_data/test_03.geojson"
    G, pos = generate_map_graph(map_file)
    nx.draw(G, pos, node_size=1)
    plt.show()
