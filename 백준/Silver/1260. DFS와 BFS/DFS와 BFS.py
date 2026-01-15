import sys
from collections import deque

# **재귀 깊이 제한 설정 (DFS 사용 시 필수)**
sys.setrecursionlimit(10**6)

# N: 정점 개수, M: 간선 개수, V: 시작 정점
N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향 그래프이므로  반대쪽도 추가

# 방문 순서를 지키기 위해 정렬
for i in range(1, N + 1):
    graph[i].sort()

# DFS
visited_dfs = [False] * (N + 1)

def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(i)

# BFS
def bfs(start):
    visited_bfs = [False] * (N + 1)
    queue = deque([start])
    visited_bfs[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                queue.append(i)


dfs(V)
print()
bfs(V)