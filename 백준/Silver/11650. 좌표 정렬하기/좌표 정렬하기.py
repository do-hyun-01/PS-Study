import sys
input = sys.stdin.readline

# 2차원 리스트로 입력 받기
points = []
for _ in range(int(input())):
    points.append(list(map(int, input().split())))

# 별도의 key 설정 없이도 x -> y 순으로 자동 정렬됨
points.sort()

for point in points:
    print(point[0], point[1])