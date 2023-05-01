from .Vertex import Vertex
from .Edge import Edge


class Graph:

    def __init__(self, vertex_list: list[Vertex] = [], directed: bool = False, weighted: bool = False):
        self.__adj_list = {}
        self.__out_adj_list: dict[Vertex, list[Vertex]] = {}  # for digraphs
        self.__directed = directed
        # self.__weighted = weighted
        for each_vertex in vertex_list:
            each_vertex.directed = directed
            if each_vertex not in self.__adj_list.keys():
                self.__adj_list.update({
                    each_vertex: []
                })

    # methods

    def add_vertex(self, vertex_list: list) -> None:
        for each_vertex in vertex_list:
            if each_vertex not in self.__adj_list.keys():
                self.__adj_list.update({
                    Vertex(each_vertex, directed=self.__directed): []
                })

    def add_edge(self,
                 src: Vertex,
                 dest: Vertex,
                 label: str = '',
                 weight: float = 0) -> None:
        # our adj list for digraph only stores vertices
        # that are connected by outwards going edges
        outgoing_edge = Edge(src, dest, label, weight, self.__directed)
        if self.__directed:
            for vertex in self.__adj_list:
                if vertex is src:
                    vertex.outgoing_edges.append(outgoing_edge)
                    vertex.key.neighbor.append(dest)
                    break
            dest.incoming_edges.append(outgoing_edge)
            self.__out_adj_list[src].append(dest)
        else:
            incoming_edge = Edge(dest, src, label, weight, self.__directed)
            for vertex in self.__adj_list:
                if vertex is src:
                    vertex.neighbors.append(dest)
                    vertex.outgoing_edges.append(outgoing_edge)
                    vertex.incoming_edges.append(incoming_edge)
                    break
            dest.neighbors.append(src)
            dest.incoming_edges.append(outgoing_edge)
            dest.outgoing_edges.append(incoming_edge)
        self.__adj_list[src].append(dest)
        self.__adj_list[dest].append(src)

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

    # properties

    @property
    def vertex_list(self) -> list[Vertex]:
        return list(self.__adj_list)

    @property
    def is_regular(self) -> bool:
        if all(x.degree ==
               list(self.__adj_list.keys())[0].degree
               for x in self.__adj_list.keys()):
            return True
        else:
            return False

    @property
    def is_complete(self) -> bool:
        total_vertices = len(self.__adj_list)
        total_edges = sum(len(self.__adj_list[x] for x in self.__adj_list))
        if total_edges == total_vertices*(total_vertices - 1)/2:
            return True
        else:
            return False

    @property
    def is_connected(self) -> bool:
        from algorithms.dfs import dfs
        list_of_vertices = set(self.__adj_list.keys())
        visited = set()
        dfs(self, next(iter(self.__adj_list)), visited)
        if visited == list_of_vertices:
            return True
        else:
            return False

    @property
    def is_regular(self) -> bool:
        return all(list(x.degree == next(iter(self.vertex_list)).degree for x in self.vertex_list))

    # this is different from a cyclic graph
    # a cycle is a connected 2-regular graph
    @property
    def is_cycle(self) -> bool:
        if self.is_connected() and self.is_regular():
            if all(list(x.degree == 2 for x in self.vertex_list)):
                return True
            else:
                return True
        else:
            return False

    def __str__(self):
        return str(self.__adj_list)
