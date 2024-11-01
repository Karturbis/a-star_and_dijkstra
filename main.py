import random
from random import randint
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

NODES_NUMBER_1 = 7
NODES_NUMBER_2 = 12
EDGE_SPAWN_PROP = 25
NODE_SPAWN_PROP = 50

SEED = randint(1, 9999999999999999999999)
random.seed(SEED)
print(SEED)

def do_with_certain_prop(prop) -> bool:
    """takes probability in percent,
    returns true, if a random with the
    given propobility is true."""
    return randint(0, 100) < prop

G = nx.Graph()
pos = {}
nodes = []
for i in range(NODES_NUMBER_1):
    for j in range(NODES_NUMBER_2):
        if do_with_certain_prop(NODE_SPAWN_PROP):
            nodes.append((i, j))
            pos[(i, j)] = np.array([i, j])

G.add_nodes_from(nodes)
for i in G.nodes():
    for k in G.nodes():
        if do_with_certain_prop(EDGE_SPAWN_PROP):
            if i != k and len(G.edges(i)) <=3 and len(G.edges(k)) <=3:
                G.add_edge(i, k)

nx.draw(G, pos, with_labels=True)
plt.show()
