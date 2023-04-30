from core.Vertex import Vertex
from core.Edge import Edge
from core.Graph import Graph
from algorithms.dfs import dfs

v0 = Vertex('0')
v1 = Vertex('1')
v2 = Vertex('2')
v3 = Vertex('3')
v4 = Vertex('4')


test_graph = Graph([v0, v1, v2, v3, v4])

test_graph.add_edge(v0, v1)
test_graph.add_edge(v1, v3)
test_graph.add_edge(v3, v2)
test_graph.add_edge(v0, v2)
test_graph.add_edge(v0, v3)
test_graph.add_edge(v3, v4)
visited = set()
dfs(test_graph, v0, visited)
print(visited)
if test_graph.is_connected():
    print('Connected')
else:
    print('Not connected')
print(test_graph.components_count())
# print(test_graph)
