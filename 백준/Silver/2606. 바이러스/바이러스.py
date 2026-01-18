import sys

input = sys.stdin.readline

n = int(input()) # 노드의 수
m = int(input()) # 간선의 수

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향 연결

# DFS 탐색 정의
visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)

print(sum(visited) - 1)