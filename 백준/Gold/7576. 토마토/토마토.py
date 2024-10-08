from collections import deque

n, m = tuple(map(int, input().split()))
arr = []
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0
visited = set()

for i in range(m):
    arr.append(list(map(int, input().split())))

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            queue.append([i, j])
            visited.add((i, j))


def bfs():
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny <= m - 1 and 0 <= nx <= n - 1 and arr[ny][nx] != -1:
                if (ny, nx) not in visited:
                    arr[ny][nx] = arr[y][x] + 1
                    queue.append([ny, nx])
                    visited.add((ny, nx))


bfs()
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 0:
            print(-1)
            exit()
        if answer < arr[i][j]:
            answer = arr[i][j]

print(answer - 1)
