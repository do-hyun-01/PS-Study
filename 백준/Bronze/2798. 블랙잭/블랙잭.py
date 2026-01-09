import sys

# 입력 받기
# N: 카드의 개수, M: 목표 숫자
N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

result = 0
length = len(cards)

# 3장의 카드를 뽑는 모든 경우의 수 탐색
# 첫 번째 카드 i
for i in range(0, length - 2):
    # 두 번째 카드 j는 i 다음부터
    for j in range(i + 1, length - 1):
        # 세 번째 카드 k는 j 다음부터
        for k in range(j + 1, length):
            sum_val = cards[i] + cards[j] + cards[k]
            
            # 합이 M을 넘지 않는 경우 중 최댓값 업데이트
            if sum_val <= M:
                result = max(result, sum_val)

print(result)