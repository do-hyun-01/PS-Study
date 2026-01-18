import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u) # 양방향 간선

# DFS 함수 정의
visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

# 모든 노드 순회, 간선 수 카운트
count = 0

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)