from core.Vertex import Vertex


class Edge:
    def __init__(self,
                 src: Vertex,
                 dest: Vertex,
                 label: str = '',
                 weight: float = 0,
                 directed: bool = False):
        self.__src = src
        self.__dest = dest
        self.__label = label
        self.__weight = weight
        self.__directed = directed

    @property
    def label(self) -> str:
        return self.__label

    @property
    def weight(self) -> float:
        return self.__weight

    @property
    def src(self) -> Vertex:
        return self.__src

    @property
    def dest(self) -> Vertex:
        return self.__dest

    @property
    def directed(self) -> bool:
        return self.__directed

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
                if ((__value.src == self.src
                        and __value.dest == self.dest)
                        or (__value.src == self.dest
                            and __value.dest == self.src)) \
                        and __value.weight == self.weight \
                        and __value.label == self.label:
                    return True
                else:
                    return False
        else:
            return False

    def __lt__(self, __value) -> bool:
        if isinstance(__value, Edge):
            return self.weight < __value.weight
        return False

    def __hash__(self) -> int:
        return hash((self.src, self.dest, self.label))

    def __repr__(self):
        if self.directed:
            return str(self.src) + ' --> ' + str(self.dest)
        else:
            return str(self.src) + ' -- ' + str(self.dest)
