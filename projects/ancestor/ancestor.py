class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

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

    def getParents(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]

def earliest_ancestor(ancestors, starting_node):
    # vetices: children
    # edge: parent-child relashionship
    # get parents returns all the parents for a child
    # Use a queue to keep track of the level and parent to check so far
    # If current parent (dequeued) is at the same level as the solution so far, save the parent with lowest id
    # if current parent is at a higher level than the solution, save that parent as the solution so far

    # Build the graph
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
    for pair in ancestors:
        graph.add_edge(pair[1], pair[0])

    # If the starting_node has no parent, return -1
    parents = graph.getParents(starting_node)
    if len(parents) == 0:
        return -1

    q = Queue()
    solution = (starting_node, 0)
    q.enqueue((starting_node, 0))    
    # Enqueue the farthest parent so far
    while q.size() > 0:
        current = q.dequeue()
        current_person = current[0]
        current_level = current[1]
        if (current_level == solution[1] and current_person < solution[0]) or current_level > solution[1]:
            # save new ancestor
            solution = current
        parents = graph.getParents(current_person)
        for parent in parents:
            q.enqueue((parent, current_level+1))
    return solution[0]



ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
ancestor = earliest_ancestor(ancestors, 3)
print(ancestor)