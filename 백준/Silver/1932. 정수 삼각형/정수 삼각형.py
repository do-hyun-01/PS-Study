import sys

input = sys.stdin.readline

n = int(input())
triangle = []

for _ in range(n):
    triangle.append(list(map(int, input().split())))

# DP
for i in range(1, n):
    for j in range(len(triangle[i])):
        #  왼쪽 끝인 경우
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        # 오른쪽 끝인 경우
        elif j == i:
            triangle[i][j] += triangle[i-1][j-1]
        # 중간인 경우
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

# 마지막 줄에서 가장 큰 값이 정답
print(max(triangle[n-1]))