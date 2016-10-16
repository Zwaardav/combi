# 7.
# Given two positive integers n and m, construct a random simple graph with n
# vertices and m edges and determine whether the graph has a Hamilton path or
# Hamilton circuit. If it has, construct such a path or circuit. If it hasn't,
# check whether there exists a subgraph by removing as little as possible nodes
# that does have a Hamilton path.

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
