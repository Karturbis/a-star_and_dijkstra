import heapq
import geopy.distance as gpd
import networkx as nx
import matplotlib.pyplot as plt

def a_star(G, start_node, end_node, heuristic):
    priority_queue = []

def distance(pos, node1, node2):
    return float(str((gpd.distance(pos[node1], pos[node2])))[:-3])

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edge("a", "b", weight=7)
    G.add_edge("a", "h", weight=3)
    G.add_edge("b", "c", weight=4)
    G.add_edge("c", "d", weight=5)
    G.add_edge("g", "d", weight=6)
    G.add_edge("g", "h", weight=2)
    G.add_edge("c", "h", weight=8)
    G.add_edge("e", "h", weight=3)
    G.add_edge("g", "e", weight=1)
    pos = nx.spring_layout(G)
    #a_star(G, "d", "a")
    print(distance(pos, "a", "b"))