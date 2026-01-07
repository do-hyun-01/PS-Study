import sys
input = sys.stdin.readline

a, b = map(int, input().split())

# 1. 최대공약수(GCD) 구하기
# 두 수 중 작은 수를 기준으로 1씩 줄여가며 찾기
gcd = 0
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        gcd = i
        break

# 2. 최소공배수(LCM) 구하기
# 공식: (A * B) / 최대공약수
lcm = (a * b) // gcd

print(gcd)
print(lcm)