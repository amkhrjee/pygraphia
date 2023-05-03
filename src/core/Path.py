from .Vertex import Vertex
from .Walk import Walk
from dataclasses import dataclass


@dataclass
class Path(Walk):

    def add(self, vertex: Vertex) -> None:
        if vertex not in self.__vertex_list:
            self.__vertex_list.append(vertex)
        else:
            pass
