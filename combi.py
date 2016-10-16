#!/bin/python
# 7.
# Given two positive integers n and m, construct a random simple graph with n
# vertices and m edges and determine whether the graph has a Hamilton path or
# Hamilton circuit. If it has, construct such a path or circuit. If it hasn't,
# check whether there exists a subgraph by removing as little as possible nodes
# that does have a Hamilton path.

import random

while True:
    vertices = input("How many vertices? n=")
    edges = input("How many edges? m=")
    try:
        vertices = int(vertices)
        edges = int(edges)
        if vertices <= 0 or edges <= 0:
            print("I'm sure those numbers will make a very nice-looking graph.")
            continue
        break
    except ValueError:
        print("Please input two integers instead")

print ("n = {}, m = {}".format(vertices, edges))

edgeobjects = []

for newedge in range(0, edges):
    v1 = random.randint(0, vertices)
    v2 = random.randint(0, vertices-1)
    if v1 == v2:
        v2 += 1
    edgeobjects.append({v1, v2})
    print("Generated edge from {} to {}".format(v1, v2))

# Now make sure edges are unique


#Generate this
g = { "a" : ["c", "b"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
        }

path = []


def hamilton ( circuit,  graph, cur_node , visited ):

	visited.append(cur_node)

	if sorted(visited) == sorted(graph.keys()):
		if circuit:
			if not cur_node == visted[0]:
				return False
		global path
		path = visited
		return True

	adjecent =  graph.get(cur_node)

	for v in adjecent:
		if v not in visited:
			found =  hamilton( circuit, graph, v , visited )
			if found:
				return True

	visited.remove(cur_node)
	return False

def hamilton_path( graph ):
	vertices = graph.keys()
	for start in vertices:
		found =  hamilton( False, graph, start, [])
		if found:
			return True
	return False

def hamilton_circuit( graph, start ):
	return hamilton ( True, graph, start, [])

if hamilton_path(g):
	print(path)
else:
	print(":(")
