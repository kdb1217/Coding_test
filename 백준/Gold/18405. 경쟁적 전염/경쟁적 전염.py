import heapq

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
arr = []

# 0부터 시작이기 때문에 1을 뺸다
x -= 1
y -= 1


def bfs(queue, s, board):
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    while queue:
        tmp = heapq.heappop(queue)
        t, v, i, j = tmp[0], tmp[1], tmp[2][0], tmp[2][1]
        if t == s:
            break
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 > ni or ni >= len(board) or 0 > nj or nj >= len(board[0]):
                continue

            if board[ni][nj] == 0:
                board[ni][nj] = v
                heapq.heappush(arr, (t + 1, board[ni][nj], (ni, nj)))


for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] != 0:
            heapq.heappush(arr, (0, board[i][j], (i, j)))

bfs(arr, s, board)

print(board[x][y])