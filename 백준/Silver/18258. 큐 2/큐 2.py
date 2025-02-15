from collections import deque
import sys

n = int(input())
dec = deque()


def push(x):
    dec.append(x)


def pop():
    if dec:
        print(dec.popleft())
    else:
        print(-1)


def size():
    print(len(dec))


def empty():
    if dec:
        print(0)
    else:
        print(1)


def front():
    if dec:
        print(dec[0])
    else:
        print(-1)


def back():
    if dec:
        print(dec[-1])
    else:
        print(-1)


for _ in range(n):
    cmd = list(sys.stdin.readline().split())

    if cmd[0] == "push":
        push(int(cmd[1]))
    elif cmd[0] == "pop":
        pop()
    elif cmd[0] == "size":
        size()
    elif cmd[0] == "empty":
        empty()
    elif cmd[0] == "front":
        front()
    else:
        back()

