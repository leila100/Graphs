
class VertexNotFound(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)
        
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices or v2 not in self.vertices:
            raise VertexNotFound("Sorry, the vertex doesn't exist")
        self.vertices[v1].add(v2)

    def getNeighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]

def earliest_ancestor(ancestors, starting_node):
    # vetices: people
    # edge: parent-child relashinship
    # get neighbors returns all the children for a parent
    # find earliest known ancestor: farthest distance from the input individual - Path with biggest number of vertices
    # Find all paths leading to input individual - return the longest
    # If two or more equal paths - return lowest numeric ID
    # If no path (the input individual has no parent) - return -1

    # Build the graph
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
    for pair in ancestors:
        graph.add_edge(pair[0], pair[1])
        print("Adding edge: ", pair[0], pair[1])

ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(ancestors, 6)