from core.Graph import Graph
from core.Vertex import Vertex
from collections import deque


def bfs(graph: Graph, start_vertex: Vertex, visited: list):
    explore_queue = deque([start_vertex])
    while len(explore_queue):
        vertex = explore_queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            for neighbor_vertices in vertex.neighbors:
                if neighbor_vertices not in visited:
                    explore_queue.append(neighbor_vertices)
