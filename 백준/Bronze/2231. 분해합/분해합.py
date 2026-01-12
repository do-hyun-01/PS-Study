import sys

N = int(sys.stdin.readline())

result = 0

for i in range(1, N):
    digit_sum = sum(map(int, str(i)))
    
    # 분해합 계산: i + (i의 각 자릿수 합)
    decomposition_sum = i + digit_sum
    
    if decomposition_sum == N:
        result = i
        break

print(result)