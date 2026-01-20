import sys
from collections import deque

input = sys.stdin.readline

n = int(input()) # 전체 사람 수
start, end = map(int, input().split()) # 촌수를 구할 두 사람
m = int(input()) # 관계의 개수

# 그래프 생성 (양방향 연결)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# BFS 탐색을 위한 준비
# visited 리스트에 '방문 여부'와 '시작점으로부터의 거리(촌수)'를 동시에 저장
# -1로 초기화하여 방문하지 않음을 표시 (0은 자기 자신과의 거리로 사용될 수 있으므로 구분)
visited = [-1] * (n + 1)

def bfs(start_node):
    queue = deque([start_node])
    visited[start_node] = 0
    
    while queue:
        current = queue.popleft()
        
        if current == end:
            return visited[end]
        
        for neighbor in graph[current]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[current] + 1
                queue.append(neighbor)
    
    return -1

print(bfs(start))