from a_star import a_star

def dijkstra(G, pos, start_node, end_node, arg1=None):
    """Finds the shortest path between two nodes,
    using Dijkstra's algorithm, which is equivalent
    to the A* algorithm with no heuristic"""
    return a_star(G, pos, start_node, end_node, None)