import sys
import heapq
from collections import deque

n, m = map(int, input().split())

s = set()
cnt = 0
for i in range(n):
    tmp = str(input())
    s.add(tmp)

for j in range(m):
    tmp = str(input())
    if tmp in s:
        cnt += 1

print(cnt)
