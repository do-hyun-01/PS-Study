import sys

input = sys.stdin.readline

n = int(input())
meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 종료 시간(x[1]), 시작 시간(x[0]) 기준으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end_time = 0

for start, end in meetings:
    # 현재 회의의 시작 시간이 이전 회의의 종료 시간보다 크거나 같다면 배정 가능
    if start >= last_end_time:
        count += 1
        last_end_time = end

print(count)