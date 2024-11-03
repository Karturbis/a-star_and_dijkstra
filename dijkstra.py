"""Contains the dijkstra function, which
uses Dijkstras Algorithm to find shortest path."""
from a_star import a_star

def dijkstra(G, pos, start_node, end_node, _=None):
    """Finds the shortest path between two nodes,
    using Dijkstra's algorithm, which is equivalent
    to the A* algorithm with no heuristic"""
    return a_star(G, pos, start_node, end_node, None)
