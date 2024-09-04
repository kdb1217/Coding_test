import sys
from collections import deque


def solution():
    n, m = map(int, input().split())
    arr = [-1] * 100005
    arr[n] = 0

    def bfs(width):
        queue = deque()
        queue.append(n)

        if n == m:
            print(0)
            return

        while queue:
            x = queue.popleft()
            for i in [x - 1, x + 1, x * 2]:
                if i == m:
                    print(arr[x] + 1)
                    sys.exit()
                if 0 <= i < len(arr):
                    if arr[i] == -1 :
                        arr[i] = arr[x] + 1
                        queue.append(i)

    bfs(n)


solution()
