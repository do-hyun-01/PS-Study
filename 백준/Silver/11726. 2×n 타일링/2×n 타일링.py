import sys

input = sys.stdin.readline
n = int(input())

# DP 테이블 초기화
# n은 최대 1,000이므로 넉넉하게 1001 크기로 생성
dp = [0] * 1001

# 초기값 설정 (Base Case)
dp[1] = 1 # 2x1 채우는 방법: 세로 1개
dp[2] = 2 # 2x2 채우는 방법: 세로 2개 or 가로 2개

# 점화식 적용 (Bottom-Up)
# 3부터 n까지 차례대로 채워 나감
for i in range(3, n + 1):
    # 문제 조건: 10,007로 나눈 나머지 출력
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[n])