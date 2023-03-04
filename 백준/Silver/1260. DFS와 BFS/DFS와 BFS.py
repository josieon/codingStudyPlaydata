import sys
from collections import deque

N, M, V = [*map(int, sys.stdin.readline().split())]

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

visited_dfs = []
visited_bfs = []

for edge in graph:
    edge.sort()

queue = deque([])

def dfs(v):
    if v not in visited_dfs:
        visited_dfs.append(v)
        for i in graph[v]:
            dfs(i)

def bfs(v):
    visited_bfs.append(v)
    queue.append(v)
    while queue:
        i = queue.popleft()
        for j in graph[i]:
            if j not in visited_bfs:
                visited_bfs.append(j)
                queue.append(j)

dfs(V)
bfs(V)

print(*visited_dfs)
print(*visited_bfs)