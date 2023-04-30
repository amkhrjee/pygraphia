class Vertex:
    def __init__(self,
                 label: str = '',
                 incoming_edges: list = [],
                 outgoing_edges: list = [],
                 directed: bool = False):
        self.label = label
        self.incoming_edges = incoming_edges
        self.outgoing_edges = outgoing_edges
        self.indegree = len(incoming_edges)
        self.outdegree = len(outgoing_edges)
        if directed:
            self.degree = self.indegree + self.outdegree
        else:
            self.degree = (self.indegree + self.outdegree)/2

    def __repr__(self):
        return self.label
