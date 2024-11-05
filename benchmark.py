"""Program to benchmark the Dijkstra and A*
Algorithm in different situations, using
nx.shortest_path() as a comparison"""
import time  # to benchmark time te algorithms need
import random  # to make automated benchmarks with random situatuins
import networkx as nx  # to implement the graph
import matplotlib.pyplot as plt  # to show the graph in case this is needed
from real_map import generate_map_graph  # to generate a graph of a real map
# to use A* algorithm with differen heuristics
from a_star import a_star
from a_star import geopy_dis
from a_star import flatearther_dis
# to use Dijkstra algorithm
from dijkstra import dijkstra

# make random Seed, so benchmarks are different, but can be recreated
SEED = random.randint(1, 22222222222222222222222222222222222)
# SEEED = 1931315997966322171689304248493832

# Parameters for the benchmark:
ITERATIONS = 100
MIN_EDGE_LENGTH = 1  # only relevant, if not real_map
MAX_EDGE_LENGTH = 100  # see above
GRAPH_SIZE = 1000  # see above
REAL_MAP = True  # determines, wether a real map, or a random graph is used
DRAW_GRAPH = True
DRAW_EDGE_LABELS = False  # WARNING, uses a lot of resources in big graphs
print(
    f"Seed = {SEED}"
)  # printing the seed at the begin, so if the program crashes, it is printed
random.seed(SEED)  # setting the random seed

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
    # messure time Dijkstra needs to complete the path search:
    td = time.time()
    path_djk = dijkstra(G, pos, node_1, node_2)
    tda += time.time() - td  # adding Dijkstras time to Dijkstras overall time
    # messure time A* with flatearther distance needs to complete the path search:
    ta = time.time()
    path_ast = a_star(G, pos, node_1, node_2, flatearther_dis)
    taa += time.time() - ta
    if REAL_MAP:
        # messure the time for A* with geopys distance function as heuristic:
        tg = time.time()
        path_gas = a_star(G, pos, node_1, node_2, geopy_dis)
        tga += time.time() - tg
    # messure the time nx needs, as a reference time
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
    nx.draw(G, pos)  # make the graph drawable
    if DRAW_EDGE_LABELS:
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)}
        )
    plt.show()  # open a window and use matplotlib to draw the graph
