import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

answer = 0 # 소수의 개수

for num in numbers:
    cnt = 0 # 약수의 개수를 세는 변수
    if num == 1:
        continue
    # 1부터 자기 자신(num)까지 다 나눠봄
    for i in range(1, num + 1):
        if num % i == 0:
            cnt += 1
    # 약수가 1과 자기자신 뿐이라면 소수
    if cnt == 2:
        answer += 1

print(answer)