from core.Graph import Graph
from core.Vertex import Vertex


def dfs(graph: Graph, start_vertex: Vertex, visited: list) -> None:
    visited.append(start_vertex)
    for each_neighbor in start_vertex.neighbors:
        if each_neighbor not in visited:
            dfs(graph, each_neighbor, visited)
