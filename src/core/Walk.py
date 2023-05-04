from .Vertex import Vertex
from dataclasses import dataclass, field
from typing import List


@dataclass()
class Walk:

    vertex_list: List[Vertex] = field(default_factory=list)
    is_empty: bool = False

    def __init__(self, vertex: Vertex | None):
        if isinstance(vertex, Vertex):
            self.vertex_list.append(vertex)
        else:
            self.is_empty = True

    def add(self, vertex: Vertex):
        self.vertex_list.append(vertex)

    def __repr__(self) -> str:
        if not self.is_empty:
            return '--'.join(str(vertex) for vertex in self.vertex_list)
        else:
            return 'No Walk'

    def __str__(self) -> str:
        if not self.is_empty:
            return '--'.join(str(vertex) for vertex in self.vertex_list)
        else:
            return 'No Walk'
