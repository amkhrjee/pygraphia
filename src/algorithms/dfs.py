from core import *


def dfs(graph: Graph, start_vertex: Vertex, visited: set) -> None:
    visited.add(start_vertex)
    for each_neighbor in start_vertex.neighbors:
        if each_neighbor not in visited:
            dfs(graph, each_neighbor, visited)
