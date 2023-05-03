from .Vertex import Vertex
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Walk:
    vertex_list: list[Vertex] = field(default_factory=list)

    # def __init_subclass__(cls, vertex: Vertex = None) -> None:
    #     cls.vertex_list.append(vertex)

    def add(self, vertex: Vertex) -> None:
        self.vertex_list.append(vertex)

    def __repr__(self) -> str:
        return '--'.join(self.__vertex_list)
