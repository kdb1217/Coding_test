from collections import deque

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(startNode, K):
    cnt = 0
    queue = deque()
    queue.append([startNode, cnt])
    visited[startNode] = True
    answer = []

    while queue:
        tmplst = queue.popleft()
        node, dist = tmplst[0], tmplst[1]
        if dist == K:
            answer.append(node)

        for i in graph[node]:
            if not visited[i]:
                queue.append([i, dist + 1])
                visited[i] = True

    return answer


result = bfs(X, K)

if len(result) > 0:
    result.sort()

    for i in result:
        print(i)
else:
    print(-1)
