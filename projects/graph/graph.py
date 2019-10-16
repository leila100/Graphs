"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

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

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        if starting_vertex not in self.vertices:
            raise VertexNotFound("Sorry, the vertex doesn't exist")
        answer = []
        visited = set()
        q = Queue()
        q.enqueue(starting_vertex)
        while q.size():
            current_vertex = q.dequeue()
            if current_vertex not in visited:
                answer.append(str(current_vertex))
                visited.add(current_vertex)
                neighbors = self.getNeighbors(current_vertex)
                if neighbors and len(neighbors):
                    for neighbor in neighbors:
                        q.enqueue(neighbor)
        print("BFT: " + " ".join(answer))
        return answer

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        if starting_vertex not in self.vertices:
            raise VertexNotFound("Sorry, the vertex doesn't exist")
        visited = set()
        answer = []
        st = Stack()
        st.push(starting_vertex)
        while st.size():
            current_vertex = st.pop()
            if current_vertex not in visited:
                answer.append(str(current_vertex))
                visited.add(current_vertex)
                neighbors = self.getNeighbors(current_vertex)
                if neighbors and len(neighbors):
                    for neighbor in neighbors:
                        st.push(neighbor)
        print("DFT: " + " ".join(answer))
        return answer

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if starting_vertex not in self.vertices:
            raise VertexNotFound("Sorry, the vertex doesn't exist")
        result = []
        visited = set()
        def dft(vertex, visited, answer):
            if vertex not in visited:
                visited.add(vertex)
                answer.append(str(vertex))
                neighbors = self.getNeighbors(vertex)
                if neighbors and len(neighbors) > 0:
                    for neighbor in neighbors:
                        dft(neighbor, visited, answer)

        dft(starting_vertex, visited, result)
        print("Recursive DFT: " + " ".join(result))
        return result

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        if starting_vertex not in self.vertices or destination_vertex not in self.vertices:
            raise VertexNotFound("Sorry, the vertex doesn't exist")
        visited = set()
        answer = []
        st = Stack()
        st.push(starting_vertex)
        while st.size():
            current_vertex = st.pop()
            if current_vertex not in visited:
                answer.append(current_vertex)
                visited.add(current_vertex)
                if current_vertex == destination_vertex:
                    return answer
                neighbors = self.getNeighbors(current_vertex)
                if neighbors and len(neighbors):
                    for neighbor in neighbors:
                        st.push(neighbor)
        





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    # graph.add_edge(4, 8)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    # graph.dft(11)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    # graph.bft(9)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)
    # graph.dft_recursive(15)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
