from collections import deque

answer = 0


def solution():
    n, m = map(int, input().split())
    arr = list()
    visited = [[False for _ in range(m)] for _ in range(n)]

    for _ in range(n):
        arr.append(list(input()))


    def getStart():
        for i in range(n):
            for j in range(m):
                if arr[i][j] == "I":
                    return i, j

    startx, starty = getStart()
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

                if arr[nx][ny] != "X":
                    if visited[nx][ny] == False:
                        queue.append((nx, ny))
                        if arr[nx][ny] == "P":
                            global answer
                            answer += 1

                visited[nx][ny] = True

    bfs(startx, starty)

solution()
if answer == 0:
    print("TT")
else:
    print(answer)
