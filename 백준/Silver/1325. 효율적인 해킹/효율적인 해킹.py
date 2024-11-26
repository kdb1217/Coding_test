from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
answer = -1
result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


def bfs(node):
    global answer, result
    queue = deque([node])
    visited = [False] * (n + 1)
    visited[node] = True
    cnt = 1

    while queue:
        cur = queue.popleft()

        for i in graph[cur]:
            if not visited[i]:
                cnt += 1
                visited[i] = True
                queue.append(i)

    if cnt > answer:
        answer = cnt
        result = [node]
    elif cnt == answer:
        result.append(node)


for i in range(1, (n + 1)):
    bfs(i)

print(*sorted(result))
