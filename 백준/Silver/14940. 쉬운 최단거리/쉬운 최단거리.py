from collections import deque


def solution():
    n, m = map(int, input().split())
    arr = []
    visited = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        arr.append(list(map(int, input().split())))

    def getStarter():
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 2:
                    return [i, j]

    startx, starty = getStarter()
    arr[startx][starty] = 0
    visited[startx][starty] = True

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if arr[nx][ny] == 1:
                    if not visited[nx][ny]:
                        arr[nx][ny] = arr[x][y] + 1
                        queue.append((nx, ny))

                if not visited[nx][ny]:
                    visited[nx][ny] = True

    bfs(startx, starty)

    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                print(arr[i][j], end=" ")
            else:
                if arr[i][j] == 0:
                    print(arr[i][j], end = " ")
                else:
                    print(-1, end=" ")
        print()

solution()
