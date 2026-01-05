import sys
input = sys.stdin.readline

numbers = []

for _ in range(9):
    numbers.append(int(input()))

# 최댓값 찾기
max_num = max(numbers)
print(max_num)

# 최댓값의 위치 찾기
print(numbers.index(max_num) + 1)