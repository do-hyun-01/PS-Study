import sys

n = int(sys.stdin.readline())

fibo_list = [0, 1]

for i in range(2, n + 1):
    next_val = fibo_list[i - 1] + fibo_list[i - 2]
    fibo_list.append(next_val)
    
print(fibo_list[n])
