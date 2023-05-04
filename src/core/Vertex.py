from __future__ import annotations
from typing import TYPE_CHECKING
from typing import List
if TYPE_CHECKING:
    from .Edge import Edge


class Vertex:

    def __init__(self,
                 label: str = '',
                 directed: bool = False):
        self.__label = label
        self.__directed = directed
        self.__incoming_edges: List[Edge] = []
        self.__outgoing_edges: List[Edge] = []
        self.__neighbors: List[Vertex] = []

    @property
    def label(self) -> str:
        return self.__label

    @property
    def directed(self) -> bool:
        return self.__directed

    @property
    def incoming_edges(self) -> list[Edge]:
        return self.__incoming_edges

    @property
    def outgoing_edges(self) -> list[Edge]:
        return self.__outgoing_edges

    @property
    def neighbors(self) -> list:
        return self.__neighbors

    @property
    def edges(self) -> List[Edge]:
        if self.directed:
            return self.incoming_edges + self.outgoing_edges
        else:
            return self.outgoing_edges

    @property
    def indegree(self) -> int:
        return len(self.incoming_edges)

    @property
    def outdegree(self) -> int:
        return len(self.outgoing_edges)

    @property
    def degree(self) -> int:
        if self.directed:
            return self.indegree + self.outdegree
        else:
            return int(
                (self.outdegree + self.indegree)/2)

    def __repr__(self):
        return self.label

    def __str__(self):
        return self.label

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Vertex):
            if __value.label == self.label:
                return True
            else:
                return False
        else:
            return False

    def __hash__(self) -> int:
        return hash(self.label)
