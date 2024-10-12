n, m, r = tuple(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]


def rotate(board):
    for i in range(min(n // 2, m // 2)):
        r1, c1, r2, c2 = i, i, (n - (i + 1)), (m - (i + 1))

        tmp = board[r1][c2]

        # 오른쩍 세로
        for x in range(r1, r2):
            board[x][c2] = board[x + 1][c2]

        # 제일 아래 열
        for x in range(c2, c1, -1):
            board[r2][x] = board[r2][x - 1]

        # 왼쪽 세로
        for x in range(r2, r1, -1):
            board[x][c1] = board[x - 1][c1]

        for x in range(c1, c2):
            board[r1][x] = board[r1][x + 1]

        board[r1][c2 - 1] = tmp

    return board

for i in range(r):
    board = rotate(board)

for i in range(n):
    print(*board[i])