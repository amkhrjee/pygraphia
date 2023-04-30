from . import Vertex


class Edge:
    def __init__(self,
                 src: Vertex,
                 dest: Vertex,
                 label: list = '',
                 weight: float = 0,
                 directed: bool = False):
        self.src = src
        self.dest = dest
        self.weight = weight
        self.directed = directed
        self.label = label

    def __repr__(self):
        return self.src + '---->' + self.dest + ' ['+self.label+']'
