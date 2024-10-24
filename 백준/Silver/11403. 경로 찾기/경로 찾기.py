from collections import deque

n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))

graph = [[] for _ in range(n)]
answer = [[0] * n for _ in range(n)]


for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            graph[i].append(j)


def bfs(lst):
    queue = deque()
    tmpList = list()
    visited = [False] * n

    for z in lst:
        queue.append(z)

    while queue:

        a = queue.popleft()
        tmpList.append(a)
        visited[a] = True


        for i in graph[a]:
            if not visited[i]:
                queue.append(i)

    return tmpList


for i in range(n):
    tmp = bfs(graph[i])

    for j in range(len(answer[i])):
        if j in tmp:
            answer[i][j] = 1


for i in answer:
    print(*i)

