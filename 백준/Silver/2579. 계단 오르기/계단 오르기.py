import sys

input = sys.stdin.readline
n = int(input())

# 계단 점수 저장용 리스트 (N은 최대 300)
# 인덱스 에러 방지를 위해 301 크기로 미리 할당
stairs = [0] * 301
for i in range(1, n + 1):
    stairs[i] = int(input())

# DP 테이블 초기화
dp = [0] * 301

# 초기값 설정 (Base Case)
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

# 점화식 적용 (Bottom-Up)
# 4번째 계단부터 n번째까지 계산
for i in range(4, n + 1):
    # 경우의 수 1: 2칸 전에서 점프해 온 경우 (dp[i-2])
    # 경우의 수 2: 3칸 전에서 점프해서, 바로 앞 계단을 밟고 온 경우 (dp[i-3] + stairs[i-1])
    # 둘 중 더 큰 값에 현재 계단 점수(stairs[i])를 더함
    dp[i] = max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i]

print(dp[n])