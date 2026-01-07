import sys
input = sys.stdin.readline

n = int(input())
# set은 내부적으로 해시를 쓰기 때문에 탐색이 빠름 (O(1))
a_set = set(map(int, input().split())) 

m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    if target in a_set:
        print(1)
    else:
        print(0)