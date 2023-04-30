from .Vertex import Vertex
from .Edge import Edge


class Graph:
    def __init__(self, vertex_list: list[Vertex] = [], directed: bool = False, weighted: bool = False):
        self.__adj_list = {}
        self.__out_adj_list = {}  # for digraphs
        self.__directed = directed
        self.__weighted = weighted
        for each_vertex in vertex_list:
            each_vertex.directed = directed
            if each_vertex not in self.__adj_list.keys():
                self.__adj_list.update({
                    each_vertex: []
                })

    def add_vertex(self, vertex_list: list):
        for each_vertex in vertex_list:
            if each_vertex not in self.__adj_list.keys():
                self.__adj_list.update({
                    Vertex(each_vertex, directed=self.__directed): []
                })

    # def add_edge(self, src: str, dest: str, label: str, weight: float):
    #     for key in self.__adj_list.keys():
    #         if key.label == src:
    #             src_vertex = key

    def add_edge(self, src: Vertex, dest: Vertex, label: str = '', weight: float = 0):
        # our adj list for digraph only stores vertices
        # that are connected by outwards going edges
        edge = Edge(src, dest, label, weight)
        if self.__weighted:
            for key in self.__adj_list.keys():
                if key is src:
                    key.outgoing_edges.append(edge)
                    key.neighbor.append(dest)
            dest.incoming_edges.append(edge)
            self.__out_adj_list[src].append(dest)
        else:
            for key in self.__adj_list.keys():
                if key is src:
                    key.neighbors.append(dest)
                    dest.neighbors.append(key)
                    key.outgoing_edges.append(edge)
                    key.incoming_edges.append(edge)
            dest.incoming_edges.append(edge)
            dest.outgoing_edges.append(edge)
        self.__adj_list[src].append(dest)
        # self.__adj_list.update({

        # })
        self.__adj_list[dest].append(src)

    def is_regular(self) -> bool:
        if all(x.degree ==
               list(self.__adj_list.keys())[0].degree
               for x in self.__adj_list.keys()):
            return True
        else:
            return False

    def is_complete(self) -> bool:
        total_vertices = len(self.__adj_list)
        total_edges = sum(len(self.__adj_list[x] for x in self.__adj_list))
        if total_edges == total_vertices*(total_vertices - 1)/2:
            return True
        else:
            return False

    # def is_connected(self) -> bool:

    def __str__(self):
        return str(self.__adj_list)
