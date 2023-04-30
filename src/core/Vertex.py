class Vertex:
    incoming_edges = []
    outgoing_edges = []
    neighbors = []

    def __init__(self,
                 label: str = '',
                 directed: bool = False):
        self.label = label
        self.indegree = len(self.incoming_edges)
        self.outdegree = len(self.outgoing_edges)
        self.directed = directed
        if directed:
            self.degree = self.indegree + self.outdegree
        else:
            self.degree = (self.indegree + self.outdegree)/2

    def __repr__(self):
        return self.label

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Vertex):
            if __value.label == self.label:
                return True
        else:
            return False

    def __hash__(self) -> int:
        return hash(self.label)
