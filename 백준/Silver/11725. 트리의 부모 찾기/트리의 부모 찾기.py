import sys
from collections import deque
sys.setrecursionlimit(10**5)

n = int(input())

graph = [[] for i in range(n + 1)]
visited = deque([0] * (n + 1))


for i in range(n - 1):
    tmp = list(map(int, input().split()))
    graph[tmp[0]].append(tmp[1])
    graph[tmp[1]].append(tmp[0])

def dfs(node):
    for i in graph[node]:
        if visited[i] == 0:
            visited[i] = node
            dfs(i)

dfs(1)
visited.popleft()
visited.popleft()
for i in visited:
    print(i)