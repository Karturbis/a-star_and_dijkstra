import time
import random
import networkx as nx
import matplotlib.pyplot as plt
from real_map import generate_map_graph
from a_star import a_star
from a_star import geopy_dis
from a_star import flatearther_dis
from dijkstra import dijkstra

SEED = random.randint(1, 22222222222222222222222222222222222)
# SEEED = 1931315997966322171689304248493832
ITERATIONS = 100
MIN_EDGE_LENGTH = 1
MAX_EDGE_LENGTH = 100
GRAPH_SIZE = 1000
REAL_MAP = True
DRAW_GRAPH = True
DRAW_EDGE_LABELS = False
print(
    f"Seed = {SEED}"
)  # printing the seed at the begin, so if the program crashes, it is printed
random.seed(SEED)

if REAL_MAP:
    G, pos = generate_map_graph()  # create a Graph from a real map
else:
    # create a random binomial Graph:
    G = nx.binomial_graph(GRAPH_SIZE, 10 / GRAPH_SIZE)
    pos = nx.spring_layout(G)
    weights = nx.edge_betweenness_centrality(G, normalized=False)
    for edge in G.edges():
        weights[edge] = random.randint(MIN_EDGE_LENGTH, MAX_EDGE_LENGTH)
    nx.set_edge_attributes(G, values=weights, name="weight")
nodes = list(G.nodes())

# init the timer sums:
tda = 0
taa = 0
tga = 0
tna = 0

for i in range(ITERATIONS):
    #node_1 = nodes[random.randint(1, len(nodes) - 1)]
    node_1 = 3428385949
    print(node_1)
    #node_2 = nodes[random.randint(1, len(nodes) - 1)]
    node_2 = 3428399062
    print(node_2)
    td = time.time()
    path_djk = dijkstra(G, pos, node_1, node_2)
    tda += time.time() - td
    ta = time.time()
    path_ast = a_star(G, pos, node_1, node_2, flatearther_dis)
    taa += time.time() - ta
    if REAL_MAP:
        taa += time.time() - ta
        tg = time.time()
        path_gas = a_star(G, pos, node_1, node_2, geopy_dis)
        tga += time.time() - tg
    tn = time.time()
    try:
        path_nx = nx.shortest_path(G, node_1, node_2, weight="weight")
    except nx.NetworkXNoPath:
        print(f"No path from {node_1} to {node_2}")
    tna += time.time() - tn

# printing the average time each algorithm needs
print(f"Average time dj: {tda/ITERATIONS}")
print(f"Average time a*: {taa/ITERATIONS}")
if REAL_MAP:
    print(f"Average time ga: {tga/ITERATIONS}")
print(f"Average time nx: {tna/ITERATIONS}")
print(
    f"The seed is: {SEED}"
)  # printing the Seed at the end of the program, so it can easily be obtained
if DRAW_GRAPH:
    nx.draw(G, pos)
    if DRAW_EDGE_LABELS:
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)}
        )
    plt.show()
