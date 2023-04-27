from edge import Edge


class Graph:
    def __init__(self, vertex_list=[], directed=False, weighted=False):
        self.__adj_list = {}
        self.__vertex_list = vertex_list
        self.__directed = directed
        self.__weighted = weighted

    def add_vertex(self, vertex_list):
        if isinstance(vertex_list, list):
            for each_vertex in vertex_list not in self.__vertex_list:
                self.__vertex_list.append(each_vertex)
        else:
            vertex = vertex_list
            if vertex not in self.__vertex_list:
                self.__vertex_list.append(vertex)

    def add_edge(self, src, dest, weight=0):
        if self.__weighted:
            if weight != 0:
                raise TypeError("Adding edge weight to an unweighted graph")
        else:
            edge = Edge(src, dest, weight)
            self.__adj_list[src] = edge
            if not self.__directed:
                self.__adj_list[dest] = edge

    def __str__(self):
        print(self.__adj_list)
