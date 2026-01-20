import sys

input = sys.stdin.readline

n = int(input())

# DP 테이블 생성
dp = [0] * (n + 1)

# 초기값 설정, dp[0]은 이미 0으로 초기화되어 있음
dp[1] = 1

# 점화식 적용 (Bottom-Up)
# 2번째부터 n번째까지 차례대로 채워 나감
for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])