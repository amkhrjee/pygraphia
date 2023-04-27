import graph


testgraph = graph.Graph(weighted=True)

vertexList = ['a', 'b', 'c']

testgraph.add_vertex(vertexList)
testgraph.add_edge('a', 'b', 'u')

print(testgraph)
