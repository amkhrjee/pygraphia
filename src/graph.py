class Edge:
    def __init__(self, src, dest, label='', weight=0, directed=False):
        self.src = src
        self.dest = dest
        self.weight = weight
        self.directed = directed
        if len(label) == 0:
            if directed:
                self.label = src + '->' + dest
            else:
                self.label = src + '-' + dest
        else:
            self.label = label

    def __repr__(self):
        return self.label


class Graph:
    def __init__(self, vertex_list=[], directed=False, weighted=False):
        self.__adj_list = {}
        self.__directed = directed
        self.__weighted = weighted
        if isinstance(vertex_list, list):
            for each_vertex in vertex_list:
                if each_vertex not in self.__adj_list.keys():
                    self.__adj_list.update({
                        each_vertex: []
                    })
        else:
            single_vertex = vertex_list
            if single_vertex not in self.__adj_list.keys():
                self.__adj_list.update({
                    single_vertex: []
                })

    def add_vertex(self, vertex_list):
        if isinstance(vertex_list, list):
            for each_vertex in vertex_list:
                if each_vertex not in self.__adj_list.keys():
                    self.__adj_list.update({
                        each_vertex: []
                    })
        else:
            single_vertex = vertex_list
            if single_vertex not in self.__adj_list.keys():
                self.__adj_list.update({
                    single_vertex: []
                })

    def add_edge(self, src, dest, label='', weight=0):
        if not self.__weighted and weight != 0:
            raise TypeError("Adding edge weight to an unweighted graph")
        else:
            edge = Edge(src, dest, label, weight)
            self.__adj_list[src].append(edge)
            if not self.__directed:
                self.__adj_list[dest].append(edge)

    def __str__(self):
        return str(self.__adj_list)
