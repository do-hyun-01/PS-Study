import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

s, e = 0, max(trees) # s : start, e : end

result = 0
while s <= e:
    mid = (s + e) // 2
    
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid
            
    if total >= m:
        result = mid
        s = mid + 1

    else:
        e = mid - 1

print(result)