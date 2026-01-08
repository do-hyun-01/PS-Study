import sys
input = sys.stdin.readline

def parChecker(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

T = int(input())

for _ in range(T):
    string = input().strip()
    if parChecker(string):
        print("YES")
    else:
        print("NO")