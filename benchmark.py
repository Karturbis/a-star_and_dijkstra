import time
import random
import networkx as nx
from real_map import generate_map_graph
from a_star import a_star
from a_star import geopy_dis
from a_star import flatearther_dis
from dijkstra import dijkstra

SEED = random.randint(1, 22222222222222222222222222222222222)
#SEEED = 1931315997966322171689304248493832
ITERATIONS = 100
print(f"Seed = {SEED}")  # printing the seed at the begin, so if the program crashes, it is printed
random.seed(SEED)

G = nx.binomial_graph(1000, 56)
pos = nx.spring_layout(G)

weights = [random.randint(0, 100 + i) for i in range(len(G.edges()))]

nx.set_edge_attributes(G, values = 6, name = 'weight')

nodes = list(G.nodes())

tda = 0
taa = 0
tga = 0
tna = 0

for i in range(ITERATIONS):

    node_1 = nodes[random.randint(1, len(nodes)-1)]
    #node_1 = 7660414077
    print(node_1)
    node_2 = nodes[random.randint(1, len(nodes)-1)]
    #node_2 = 271900861
    print(node_2)
    td = time.time()

    path_djk = dijkstra(G, pos, node_1, node_2)
    tda += time.time() - td
    ta = time.time()
    try:
        path_ast = a_star(G, pos, node_1, node_2, flatearther_dis)
    except Exception:
        print(f"Error {e.message} has occured")
    taa += time.time() - ta
    """tg = time.time()
    try:
        path_gas = a_star(G, pos, node_1, node_2, geopy_dis)
    except Exception:
        print(f"Error {e} has occured")
    tga += time.time() - tg"""
    tn = time.time()

    path_nx = nx.shortest_path(G, node_1, node_2, weight="weight")

    tna += time.time() - tn

# printing the average time each algorithm needs
print(f"Average time dj: {tda/ITERATIONS}")
print(f"Average time a*: {taa/ITERATIONS}")
print(f"Average time ga: {tga/ITERATIONS}")
print(f"Average time nx: {tna/ITERATIONS}")
print(f"The seed is: {SEED}")  # printing the Seed at the end of the program, so it can easily be obtained