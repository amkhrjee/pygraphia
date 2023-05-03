from .Vertex import Vertex
from dataclasses import dataclass, field


@dataclass()
class Walk:

    vertex_list = []

    def __init__(self, vertex: Vertex = None) -> None:
        self.vertex_list.append(vertex)

    def add(self, vertex: Vertex) -> None:
        self.vertex_list.append(vertex)

    def __repr__(self) -> str:
        return '--'.join(self.vertex_list)

    def __str__(self) -> str:
        return '--'.join(str(v) for v in self.vertex_list)
