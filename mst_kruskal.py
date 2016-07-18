import numpy

parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return minimum_spanning_tree

nodes = input("Enter the number of nodes")
file_name = "AdjacencyMatrix_of_Graph_G_N_%s.txt" % nodes
adj_matrix = []
with open(file_name) as ADJ:
    for line in ADJ:
        adj_matrix.append(list(filter(None,line.strip().lstrip().split('   '))))
vertices = []
edges = []
rows = len(adj_matrix)
cols = len(adj_matrix[0])
for row in range(rows):
    for col in range(cols):
        #import pdb; pdb.set_trace()
        #edges.append((int(adj_matrix[row][col].lstrip()), str(row), str(col)))
        edges.append((int(adj_matrix[row][col].lstrip()), row, col))
    vertices.append(row)

import pdb; pdb.set_trace()
graph = {'vertices': vertices, 'edges': set(edges)}
out_graph = kruskal(graph)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
Output section of the program
"""
print ("Total number of nodes = %s" % len(vertices))
print ("Total number of edges in the minimum spanning three = %s" % len(out_graph))
print ("List of edges & their costs:")
for row in out_graph:
    print ('(%s,%s) edge cost: %s' %(row[1], row[2], row[0]))
print ("Total cost of minimum spanning three is= ",)
suma = []
for row in out_graph:
    suma.append(row[0])
print (sum(suma))

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
