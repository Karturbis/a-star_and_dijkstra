import heapq
import math
import geopy.distance as gpd
import networkx as nx
import matplotlib.pyplot as plt


def a_star(G, pos, start_node, end_node, heuristic):
    """Finds the shortest Path between to nodes
    in a given Graph using the A* algorithm."""
    if not heuristic:
        heuristic = none_heuristic
    priority_queue = []  # Binary Heap
    heapq.heappush(
        priority_queue,
        (heuristic(pos, start_node, end_node), start_node, (0, start_node)),
    )
    visited = {start_node:(0, start_node)}
    shortest_path_finished = {}

    if start_node == end_node:
        print("Startnode equals endnode.")
        return 0, start_node

    while priority_queue:
        # Extract values from the element with smallest heuristic and
        # delete it from the priority_queue:
        _, current_node, current_spf = heapq.heappop(priority_queue)
        # check if node is already finished:
        if current_node in shortest_path_finished:
            continue
        # loop over every neighbour of the current node
        for current_neighbour, current_edge in G[current_node].items():
            current_edge = current_edge["weight"]
            # check if path to the neighbour has to be updated:
            if (
                not current_neighbour in visited
                or (current_spf[0] + current_edge) < visited[current_neighbour][0]
            ):
                current_neighbour_spf = (current_spf[0] + current_edge, current_node)
                # sets the shortest path value in visited to shortest path and parent:
                visited[current_neighbour] = current_neighbour_spf
                # updates the priority queue
                heapq.heappush(
                    priority_queue,
                    (
                        # heuristic:
                        heuristic(pos, current_neighbour, end_node)
                        + current_neighbour_spf[0],
                        # node:
                        current_neighbour,
                        # current shortest path:
                        current_neighbour_spf,
                    ),
                )
        # finish the current node
        shortest_path_finished[current_node] = visited[current_node]
        if current_node == end_node:
            break
    path_data = []
    parent = end_node
    while not parent == start_node:
        try:
            path_data.append(shortest_path_finished[parent])
            parent = shortest_path_finished[parent][1]
        except KeyError:
            print(f"No path from {start_node} to {end_node}.")
            return 0, None
    pathlength = path_data[0][0]
    path = [i[1] for i in path_data]
    path.reverse()
    path.append(end_node)
    return pathlength, path


def geopy_dis(pos, node1, node2):
    """Function returns the geopraphical
    distance between to nodes in km as float."""
    return float(str((gpd.distance(pos[node1], pos[node2])))[:-3])

def flatearther_dis(pos, node1, node2):
    """Returns the distance betwenn to nodes,
    pretending the earth is a flat surface."""
    return math.sqrt(abs(pos[node1][0] - pos[node2][0])**2 + abs(pos[node1][1] - pos[node2][1])**2)

def none_heuristic(*arg):
    return 0

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
    print(a_star(G, pos, "d", "a", None))
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(
    G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)}
)
    plt.show()
