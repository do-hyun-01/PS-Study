import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# DP 테이블 초기화
dp = [0] * n
dp[0] = nums[0]

# DP
for i in range(1, n):
    # (이전까지의 최댓값 + 현재 숫자)와 (현재 숫자 자체)를 비교
    dp[i] = max(dp[i-1] + nums[i], nums[i])

# DP 테이블에 저장된 값 중 가장 큰 것이 정답
print(max(dp))