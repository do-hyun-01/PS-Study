import sys
N, K = map(int, sys.stdin.readline().split())

coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

# 큰 동전부터 확인하기 위해 내림차순 정렬
coins.sort(reverse=True)

count = 0

for coin in coins:
    if K >= coin:
        count += (K // coin)
        K = (K % coin)
        
    if K == 0:
        break

print(count)