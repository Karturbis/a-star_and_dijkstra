import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import json

map_file = "testmap.geojson"

with open(map_file) as map_data_raw:
    map_data = json.load(map_data_raw)


map_data_nodes = {}
map_data_edges = {}


for element in map_data["elements"]:
    if element["type"] == "node":
        map_data_nodes[element["id"]] = (element["lat"], element["lon"])
    elif element["type"] == "way":
        map_data_edges[element["id"]] = element["nodes"]

G = nx.Graph()
pos = {}
nodes = []

for node, position in map_data_nodes.items():
    nodes.append(node)
    pos[node] = np.array([position[0], position[1]])

G.add_nodes_from(nodes)

nx.draw(G, pos, node_size = 1)
plt.show()
