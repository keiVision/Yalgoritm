import sys

n_vertex, n_edge = map(int, sys.stdin.readline().split())
if n_vertex > 1000:
    raise ValueError('Vertices count is too big. Write number between 1 and 1000.')
if n_edge > 5 * 100000:
    raise ValueError('Edge count is too big. Wrtie numb between 1 and 500000')

connections = []
for i in range(n_edge):
    connections.append(list(map(int, sys.stdin.readline().split())))

adj_list = {i: set() for i in range(1, n_vertex + 1)}
for vertex, edge in connections:
    adj_list[vertex].add(edge)
    adj_list[edge].add(vertex)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

visited = dfs(adj_list, start=1)
tmp = sorted(list(visited))
print(len(tmp))
print(' '.join(map(str, sorted(visited))))


