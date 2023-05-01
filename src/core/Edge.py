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

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Edge):
            if self.directed:
                if __value.src == self.src \
                        and __value.dest == self.dest \
                        and __value.weight == self.weight \
                        and __value.label == self.label:
                    return True
                else:
                    return False
            else:
                if (__value.src == self.src
                        and __value.dest == self.dest) \
                        or (__value.src == __value.dest
                            and __value.dest == self.src) \
                        and __value.weight == self.weight \
                        and __value.label == self.label:
                    return True
                else:
                    return False
        else:
            return False

    def __hash__(self) -> int:
        return hash((self.src, self.dest, self.label))

    def __repr__(self):
        return str(self.src) + ' --> ' + str(self.dest)
