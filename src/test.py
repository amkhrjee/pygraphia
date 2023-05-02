from core.Vertex import Vertex
from core.Graph import Graph
from algorithms.dfs import dfs
from algorithms.bfs import bfs

v0 = Vertex('0')
v1 = Vertex('1')
v2 = Vertex('2')
v3 = Vertex('3')
v4 = Vertex('4')
vTest = Vertex('test')

test_graph = Graph([v0, v1, v2, v3, v4])

test_graph.add_edge(v0, v1)
test_graph.add_edge(v1, v3)
test_graph.add_edge(v3, v2)
test_graph.add_edge(v0, v2)
test_graph.add_edge(v0, v3)
test_graph.add_edge(v3, v4)
# test_graph.add_edge(v3, vTest)

visited_bfs = []
bfs(test_graph, v0, visited_bfs)
print(visited_bfs)

visited_dfs = []
dfs(test_graph, v0, visited_dfs)
print(visited_dfs)
if test_graph.is_connected:
    print('Connected')
else:
    print('Not connected')
# print(test_graph.components_count())
if (test_graph.is_regular):
    print('Regular')
else:
    print('Not Regular')
# print(test_graph)
if (test_graph.is_cyclic):
    print('Cyclic')
else:
    print('Acyclic')

if (test_graph.is_tree):
    print('Tree')
else:
    print('Not a tree')

if (test_graph.is_eulerian):
    print('Eulerian')
else:
    print('Not Eulerian')
# print the vertex sets
# for vertex in test_graph.vertex_list:
#     print(vertex,  " = ", vertex.neighbors)

print(test_graph.get_shortest_path(v0, v4))
