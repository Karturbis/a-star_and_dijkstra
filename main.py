import networkx as nx
import matplotlib.pyplot as plt
from real_map import generate_map_graph
from dijkstra import dijkstra

G, pos = generate_map_graph()
nx.draw(G, pos, node_size = 1)
plt.show()
