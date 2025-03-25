import sys

print(f'[LOG] START: Enter the number of vertices and edges: ')
n_vertex, n_edge = map(int, sys.stdin.readline().split())
print(f'[LOG] Vertices count: {n_vertex} , Edges count: {n_edge}')
if n_vertex > 1000:
    raise ValueError('Vertices count is too big. Write number between 1 and 1000.')
if n_edge > 5 * 100000:
    raise ValueError('Edge count is too big. Wrtie numb between 1 and 500000')

print(f'[LOG] Listening input of edges:')
connections = []
for i in range(n_edge):
    connections.append(list(map(int, sys.stdin.readline().split())))
print(connections)

adj_list = {i: [] for i in range(1, n_vertex + 1)}

print(f'[LOG] Filling the adjacency list: ')
for row in connections:
    vertex, edge = row

    if not edge in adj_list[vertex]:
        adj_list[vertex].append(edge)

    if not vertex in adj_list[edge]:
        adj_list[edge].append(vertex)
print(f'[LOG] Adjacency list is: \n\t{adj_list}')

for key, value in adj_list.items():
    adj_list[key] = set(value)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(f'[LOG] START DFS. Visited: {visited}')
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

visited = dfs(adj_list, start=1)
print(f'[LOG] Updated visited: \n{sorted(list(visited))}')
tmp = sorted(list(visited))
for idx in range(tmp.__len__()):
    tmp[idx] = str(tmp[idx])
print(' '.join(tmp))

# TODO : // Оптимизировать решение по скорости исполнения. 
