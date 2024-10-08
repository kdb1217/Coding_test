import sys
import heapq
from collections import deque

n = int(sys.stdin.readline())

heap = []

for i in range(n):
    num = int(sys.stdin.readline())

    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(num), num))
