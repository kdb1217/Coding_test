import heapq
import sys

heap = []
n = int(input())

for i in range(n):
    num = int(sys.stdin.readline()) * -1
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap) * -1)
    else:
        heapq.heappush(heap,num)