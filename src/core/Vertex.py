class Vertex:
    def __init__(self,
                 label: str = '',
                 directed: bool = False):
        self.label = label
        self.directed = directed
        self.incoming_edges = []
        self.outgoing_edges = []
        self.neighbors = []

    @property
    def edges(self) -> int:
        if self.directed:
            return self.incoming_edges + self.outgoing_edges
        else:
            return self.incoming_edges

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

    def __hash__(self) -> int:
        return hash(self.label)
