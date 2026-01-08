import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    command = input().split() # 명령어를 공백 기준으로 분리
    cmd = command[0]

    if cmd == 'push':
        stack.append(int(command[1]))
        
    elif cmd == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
            
    elif cmd == 'size':
        print(len(stack))
        
    elif cmd == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
            
    elif cmd == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])