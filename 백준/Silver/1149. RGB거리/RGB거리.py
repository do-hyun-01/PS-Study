import sys

input = sys.stdin.readline

n = int(input())
costs = []
for _ in range(n):
    costs.append(list(map(int, input().split())))

# DP 
for i in range(1, n):
    # i번째 집이 빨강(0)일 때: 이전 집은 초록(1)or파랑(2)
    costs[i][0] += min(costs[i-1][1], costs[i-1][2])
    
    # i번째 집이 초록(1)일 때: 이전 집은 빨강(0)or파랑(2)
    costs[i][1] += min(costs[i-1][0], costs[i-1][2])
    
    # i번째 집을 파랑(2)일 때: 이전 집은 빨강(0)or초록(1)
    costs[i][2] += min(costs[i-1][0], costs[i-1][1])

# 마지막 집의 세 가지 색상 비용 중 최솟값이 정답
print(min(costs[n-1]))