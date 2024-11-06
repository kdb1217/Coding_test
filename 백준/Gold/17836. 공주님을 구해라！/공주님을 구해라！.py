import copy
from collections import deque

n, m, t = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
normalAnswer = 0
swordDistance = 0
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
swordLocate = [-1, -1]


def normalbfs(start):
    global normalAnswer, swordDistance, swordLocate
    board = copy.deepcopy(arr)
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append(start)
    locate = []
    visited[start[0]][start[1]] = True

    while queue:
        ci, cj = queue.popleft()

        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]

            if (0 <= ni < n and 0 <= nj < m) and not visited[ni][nj]:
                if board[ni][nj] != 1:
                    if board[ni][nj] == 2:
                        swordLocate = [ni, nj]
                        swordDistance = board[ci][cj] + 1
                    board[ni][nj] = board[ci][cj] + 1
                    queue.append([ni, nj])
                    visited[ni][nj] = True
    normalAnswer = board[n - 1][m - 1]
    return locate


normalbfs((0, 0))




def swordbfs(swordLocate, swordNum):
    global swordDistance
    board = copy.deepcopy(arr)
    queue = deque()
    queue.append(swordLocate)
    visited = [[False] * m for _ in range(n)]
    visited[swordLocate[0]][swordLocate[1]] = True
    board[swordLocate[0]][swordLocate[1]] = swordNum

    while queue:
        ci, cj = queue.popleft()

        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]

            if (0 <= ni < n and 0 <= nj < m) and not visited[ni][nj]:
                board[ni][nj] = board[ci][cj] + 1
                queue.append((ni, nj))
                visited[ni][nj] = True

    swordDistance = board[n - 1][m - 1]


if swordLocate != [-1, -1]:
    swordbfs(swordLocate, swordDistance)

if swordDistance < 1 and normalAnswer < 1:
    print("Fail")
else:
    answer = list((filter(lambda x: 0 < x <= t, [swordDistance, normalAnswer])))
    if answer:
        print(min(answer))
    else:
        print("Fail")

