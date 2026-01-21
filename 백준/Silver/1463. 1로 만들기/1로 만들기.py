import sys

n = int(sys.stdin.readline())

# dp[i]는 i를 1로 만드는 최소 횟수를 저장
dp = [0] * (n + 1)

# 2부터 n까지 차례대로 최소 횟수를 구함 (Bottom-Up)
for i in range(2, n + 1):
    # (i-1을 만드는 횟수) + 1번의 연산
    dp[i] = dp[i - 1] + 1
    
    # 2로 나누어 떨어지는 경우, 더 적은 횟수인지 비교
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
        
    # 3으로 나누어 떨어지는 경우, 더 적은 횟수인지 비교
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])