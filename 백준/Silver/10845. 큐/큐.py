import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range(n):
    command = input().split() # 명령어를 공백 기준으로 분리
    cmd = command[0]

    if cmd == 'push':
        queue.append(int(command[1]))
        
    elif cmd == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
            
    elif cmd == 'size':
        print(len(queue))
        
    elif cmd == 'empty':
        if not queue:
            print(1)
        else:
            print(0)

    elif cmd == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])

    elif cmd == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])