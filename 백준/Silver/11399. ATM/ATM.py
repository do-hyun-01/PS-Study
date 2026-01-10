import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))

P.sort()

total_sum = 0
current_waiting = 0

for time in P:
    current_waiting += time 
    total_sum += current_waiting

print(total_sum)