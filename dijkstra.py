from a_star import a_star

def dijkstra(G, start_node, end_node):
    return a_star(G, start_node, end_node, None, None)