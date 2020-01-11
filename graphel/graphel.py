class Node:
    def __init__(self, name, edges, parent):
        self.name = name
        self.edges = edges
        self.parent = parent


class Edge:
    def __init__(self, name, origin, destination, weight):
        self.name = name
        self.origin = origin
        self.destination = destination
        self.weight = weight


class Graph:
    def __init__(self, name, nodes):
        self.name = name
        self.nodes = nodes
