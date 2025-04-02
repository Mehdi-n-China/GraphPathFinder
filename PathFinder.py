
import heapq
import random
import sys

def SearchNeighbors(current_distance, current_node, pq, distances, previous_nodes, graph):
    if debug == True:
        print(f"Current Node: {current_node} with distance : {current_distance}")
    for neighbor, weight in graph[current_node].items():
        distance = current_distance + weight
        if distance < distances[neighbor]:
            distances[neighbor] = distance
            previous_nodes[neighbor] = current_node
            heapq.heappush(pq, (distance, neighbor))

def CheckStatus(current_node, distances, previous_nodes, start, end):
    if current_node == end:
        path = []
        while previous_nodes[current_node] is not None:
            path.insert(0, current_node)
            current_node = previous_nodes[current_node]
        path.insert(0, start)
        return path, distances[end]
    return None, None

def GetPath(graph, start, end):

    pq = [(0, start)]
    if debug == True:
        print("Loaded Config")

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    if debug == True:
        print("Graph Loaded")

    previous_nodes = {node: None for node in graph}
    if debug == True:
        print("Preparing Node Cache")

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        path, path_distance = CheckStatus(current_node, distances, previous_nodes, start, end)
        if path:
            return path, path_distance

        SearchNeighbors(current_distance, current_node, pq, distances, previous_nodes, graph)

    return None, float('inf')

def Loading(i, bar_total):
    i += 1
    percent = round(float((i / bar_total) * 100), 2)
    bar = ('-' * int(20 * (i / bar_total))).ljust(20)
    sys.stdout.write(f'\r[{bar}] {percent}% [{i}/{bar_total}]')
    sys.stdout.flush()
    if percent == 100:
        print(" Done!")
        i = 0

def GenerateGraph(num_nodes, min_edges_per_node, max_edges_per_node, max_weight):
    graph = {}

    for node in range(1, num_nodes + 1):
        graph[node] = {}

    for node in range(1, num_nodes + 1):
        num_edges = random.randint(min_edges_per_node, max_edges_per_node)
        possible_neighbors = list(range(1, num_nodes + 1))
        possible_neighbors.remove(node)

        neighbors = random.sample(possible_neighbors, min(num_edges, len(possible_neighbors)))

        for neighbor in neighbors:
            weight = random.randint(1, max_weight)
            graph[node][neighbor] = weight
            graph[neighbor][node] = weight
        Loading(node-1, num_nodes)
    return graph

graph = GenerateGraph(num_nodes=69420, min_edges_per_node=69, max_edges_per_node=420, max_weight=69420)

"""
Use this as a format. (This is what the GenerateGraph func returns.)
graph = {
    1: {2: 1, 7: 3, 9: 7},
    2...
}
"""

global debug
debug = True

start = 42069
end = 69420
path, distance = GetPath(graph, start, end)
print(f"The shortest path from {start} to {end} is: {path} with distance {distance}")

