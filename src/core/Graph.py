from .Vertex import Vertex
from .Edge import Edge


class Graph:

    def __init__(self, vertex_list: list[Vertex] = [], directed: bool = False, weighted: bool = False):
        self.__adj_list = {}
        self.__out_adj_list: dict[Vertex, list[Vertex]] = {}  # for digraphs
        self.__directed = directed
        self.__weighted = weighted
        for each_vertex in vertex_list:
            each_vertex.directed = directed
            if each_vertex not in self.__adj_list.keys():
                self.__adj_list.update({
                    each_vertex: []
                })

    def add_vertex(self, vertex_list: list) -> None:
        for each_vertex in vertex_list:
            if each_vertex not in self.__adj_list.keys():
                self.__adj_list.update({
                    Vertex(each_vertex, directed=self.__directed): []
                })

    def add_edge(self, src: Vertex, dest: Vertex, label: str = '', weight: float = 0) -> None:
        # our adj list for digraph only stores vertices
        # that are connected by outwards going edges
        edge = Edge(src, dest, label, weight)
        if self.__weighted:
            for key in self.__adj_list.keys():
                if key == src:
                    key.outgoing_edges.add(edge)
                    key.neighbor.add(dest)
            dest.incoming_edges.add(edge)
            self.__out_adj_list[src].append(dest)
        else:
            for key in self.__adj_list.keys():
                if key == src:
                    self.__adj_list[key].append(dest)
                    key.incoming_edges.add(edge)
                    # key.outgoing_edges.add(edge)

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

    def is_connected(self) -> bool:
        from algorithms.dfs import dfs
        list_of_vertices = set(self.__adj_list.keys())
        visited = set()
        dfs(self, next(iter(self.__adj_list)), visited)
        if visited == list_of_vertices:
            return True
        else:
            return False

    def components_count(self) -> int:
        from algorithms.dfs import dfs
        start_vertex = next(iter(self.__adj_list))
        temp_vertices = [start_vertex]
        list_of_vertices = set(self.__adj_list.keys())
        for each_vertex in temp_vertices:
            visited = set()
            dfs(self, each_vertex, visited)
            left_out_vertices = [
                x for x in list_of_vertices if x not in visited]
            if len(left_out_vertices) > 0:
                temp_vertices.append(next(iter(left_out_vertices)))
        return len(temp_vertices)

    def is_regular(self) -> bool:
        list_of_vertices = list(self.__adj_list.keys())
        # return all(vertex.degree == next(iter(list_of_vertices)).degree for vertex in list_of_vertices)
        for each_vertex in list_of_vertices:
            incoming_edges = each_vertex.incoming_edges
            print(str(incoming_edges))
            print(each_vertex.degree)

    # this is different from a cyclic graph
    # def is_cycle_graph(self) -> bool:
    #     if len(self.__adj_list.keys()) > 2:
    #         if self.is_connected() and

    def __str__(self):
        return str(self.__adj_list)
