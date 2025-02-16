import sys
n = int(input())
stack = []


def push(x):
    stack.append(x)


def pop():
    if stack:
        print(stack.pop())
    else:
        print(-1)


def size():
    print(len(stack))


def empty():
    if stack:
        print(0)
    else:
        print(1)


def top():
    if stack:
        print(stack[-1])
    else:
        print(-1)


for _ in range(n):
    cmd = list(sys.stdin.readline().split())

    if cmd[0] == "push":
        push(cmd[1])
    elif cmd[0] == "pop":
        pop()
    elif cmd[0] == "size":
        size()
    elif cmd[0] == "empty":
        empty()
    else:
        top()


