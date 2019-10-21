"""
:Author: James Sherratt
:Date: 20/10/2019
:License: MIT

:name: graph.py
"""


class Graph:

    def __init__(self):
        self.vertices = set()
        self.edges = set()

    def add_vertex(self, vert):
        """
        Add a vertex to the graph.

        :param vert: name of the vertex.
        :return: None
        """
        self.vertices.add(vert)

    def add_edge(self, vert1, vert2, directional=False):
        """
        Add an edge to the graph. The edge will be defined as a simple tuple where:
        - The first value is the initial edge.
        - The second is the final edge.
        - The third is whether the edge is directional.

        :param vert1: the start vertex.
        :param vert2: the end vertex.
        :param directional: whether or not the edge has a direction. Default: False
        :return: None
        """
        self.vertices.add(vert1)
        self.vertices.add(vert2)
        if (not directional) and (vert1 > vert2):
            # swap if not directional to avoid duplicates in the set.
            self.edges.add((vert2, vert1, directional))
        else:
            self.edges.add((vert1, vert2, directional))

    def adjacency(self, vert1, vert2):
        """
        Check if 2 vertices are adjacent (if they exist). Note: if vert1 and vert2
        are connected, but directionally from vert2 to vert1, False is returned.

        :param vert1: The first vertex to compare.
        :param vert2: The second vertex to compare.
        :return: True if adjacent, False if not, None if either are not in the set.
        """
        if (vert1 not in self.vertices) or (vert2 not in self.vertices):
            return None

        for edge in self.edges:
            if (vert1 == edge[0]) and (vert2 == edge[1]):
                return True
            if (not edge[2]) and ((vert1 == edge[1]) and (vert2 == edge[0])):
                return True
        return False

    def neighbours(self, vert):
        """
        Get the neighbours of a vertex.
        :param vert: name of the vertex.
        :return: list of neighbours, or None if the vertex is not in the graph.
        """
        if vert not in self.vertices:
            return None

        neighbours = set()
        for edge in self.edges:
            if vert == edge[0]:
                neighbours.add(edge[1])
            elif (not edge[2]) and (vert == edge[1]):
                neighbours.add(edge[0])
        return neighbours

    def as_dict(self):
        """
        Convert the graph to a dictionary where:
        - Each key is a vertex.
        - Each value is a set of neighbours you can travel to.

        :return: dict representing the graph.
        """
        graph_dict = {v: set() for v in self.vertices}
        for edge in self.edges:
            graph_dict[edge[0]].add(edge[1])
            if not edge[2]:
                graph_dict[edge[1]].add(edge[0])

        return graph_dict


if __name__ == "__main__":
    mygraph = Graph()
    mygraph.add_edge("a", "b")
    mygraph.add_edge("b", "c")
    mygraph.add_edge("b", "d")
    mygraph.add_edge("c", "b")
    mygraph.add_edge("a", "e", directional=True)
    mygraph.add_vertex("z")
    print("b neighbours:", mygraph.neighbours("b"))
    print("a neighbours:", mygraph.neighbours("a"))
    print("q neighbours:", mygraph.neighbours("q"))
    print("e neighbours:", mygraph.neighbours("e"))
    print()
    # Adjacency has direction.
    print("a and e adjacent:", mygraph.adjacency("a", "e"))
    print("e and a adjacent:", mygraph.adjacency("e", "a"))
    print("d and b adjacent", mygraph.adjacency("d", "b"))
    print("q and a adjacent:", mygraph.adjacency("q", "a"))
    print("z and a adjacent:", mygraph.adjacency("z", "a"))
    print()
    print("as dict")
    print(mygraph.as_dict())

    # Exercise/ project: add a method "path" to find path between 2 vertices.
    # (Hint: lookup DFS/ BFS algorithm.)
