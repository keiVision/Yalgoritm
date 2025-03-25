import sys

class Graph:
    def __init__(self):
        self.n_vertices = 0
        self.n_edges = 0
        self.adj_list = {}

    def listen_input(self) -> list:
        self.n_vertices, self.n_edges = map(int, sys.stdin.readline().split())
        connections = []
        for _ in range(self.n_edges):
            connections.append(list(map(int, sys.stdin.readline().split())))
        return connections
    
    def create_graph(self, connections: list) -> None:
        self.adj_list = {i: set() for i in range(1, self.n_vertices + 1)}
        for v1, v2 in connections:
            self.adj_list[v1].add(v2)
            self.adj_list[v2].add(v1)
    
    def dfs_iterative(self, vertex, visited, component):
        stack = [vertex]
        while stack:
            v = stack.pop()
            if v not in visited:
                visited.add(v)
                component.append(v)
                stack.extend(self.adj_list[v])
    
    def find_connected_components(self):
        visited = set()
        components = []
        
        for vertex in range(1, self.n_vertices + 1):
            if vertex not in visited:
                component = []
                self.dfs_iterative(vertex, visited, component)
                components.append(component)
        return components

if __name__ == "__main__":
    graph = Graph()
    connections = graph.listen_input()
    graph.create_graph(connections)
    
    components = graph.find_connected_components()
    
    print(len(components))
    for component in components:
        print(len(component))
        print(" ".join(map(str, sorted(component))))
