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
		maxedges = int((vertices**2-vertices)/2)
		if edges > maxedges:
			print("I have to make a simple graph, you know.")
			continue
		break
	except ValueError:
		print("Please input two integers instead.")

print ("n = {}, m = {}".format(vertices, edges))

#edgeobjects = []

#for newedge in range(0, edges):
	#v1 = random.randint(0, vertices)
	#v2 = random.randint(0, vertices-1)
	#if v1 == v2:
		#v2 += 1
	#edgeobjects.append({v1, v2})
	#print("Generated edge from {} to {}".format(v1, v2))

# Now make sure edges are unique


#Generate this
#g = { "a" : ["c", "b"],
		#"b" : ["c", "e"],
		#"c" : ["a", "b", "d", "e"],
		#"d" : ["c"],
		#"e" : ["c", "b"],
	#}


def generate_graph(vertices, edges):
	g = {}
	e = [False]*maxedges
	
	try:
		for en in range(0, edges):
			chosen = random.randint(0,maxedges-en-1)
			print("For edge #{} in range 0,{}, calculated random number {} between 0 and {}.".format(en, edges, chosen, maxedges-en-1))
			i = 0
			while True:
				if e[i]:
					# Already an edge here
					print("Already an edge at {}, so changing chosen loc {} to {}".format(i, chosen, chosen+1))
					chosen += 1
				if i < chosen:
					i += 1
				else:
					e[i] = True
					print("Ended up putting it at {}".format(i))
					break
	except IndexError:
		print("{} is out of bounds! Max number of edges: {}".format(i, maxedges))

	edgeoffset = 0

	for v in range(0, vertices):
		g[v] = []

		# Apply the edges in the final graph
		connectingedge = v+1
		for applyedge in range(edgeoffset, edgeoffset+(vertices-(v+1))):
			if e[applyedge]:
				g[v].append(connectingedge)
			connectingedge += 1

		for duplicatable in range(0, v):
			if v in g[duplicatable]:
				g[v].append(duplicatable)
		edgeoffset += vertices-(v+1)
	print(g)
	return g

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

g = generate_graph(vertices, edges)

if hamilton_path(g):
	print(path)
else:
	print(":(")
