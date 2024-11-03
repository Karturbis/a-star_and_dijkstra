import time
import networkx as nx
from real_map import generate_map_graph
from a_star import a_star
from a_star import geopy_dis
from a_star import flatearther_dis
from dijkstra import dijkstra

G, pos = generate_map_graph()
node_1 = 1770439267
node_2 = 11201847066

t = time.time()
path_djk = dijkstra(G, pos, node_1, node_2)
print(f"Dijkstra finished in {time.time() - t}")
t = time.time()
path_ast = a_star(G, pos, node_1, node_2, flatearther_dis)
print(f"A* finished in: {time.time() - t}")
t = time.time()
path_nx = nx.shortest_path(G, node_1, node_2)
print(f"Networkx finished in {time.time() -t}")
print("-----------------------------------")
print(path_djk)
print(path_ast)
print(path_nx)
print("-----------------------------------")
print(nx.shortest_path_length(G, node_1, node_2))