n, m = tuple(map(int, input().split()))
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x, visited, cnt):
    global answer

    if cnt == 4:
        answer = 1
        return

    visited[x] = True

    for i in graph[x]:
        if not visited[i]:
            dfs(i, visited, cnt + 1)

    visited[x] = False


for i in range(n):
    answer = 0
    visited = [False for _ in range(n)]
    dfs(i, visited, 0)
    if answer == 1:
        print(answer)
        exit()

print(answer)

