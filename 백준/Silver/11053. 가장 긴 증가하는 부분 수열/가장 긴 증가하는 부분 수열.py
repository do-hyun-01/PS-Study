import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# dp[i]는 a[i]를 마지막 원소로 가지는 LIS의 길이
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        # 현재 값이 이전 값보다 크면 증가 수열 가능
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# dp 테이블에 저장된 값 중 최대치가 수열 전체의 LIS 길이
print(max(dp))