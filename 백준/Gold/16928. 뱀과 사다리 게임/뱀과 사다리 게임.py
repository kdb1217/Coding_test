from collections import deque

n, m = tuple(map(int, input().split()))

ladder = [tuple(map(int, input().split())) for _ in range(n)]
snakes = [tuple(map(int, input().split())) for _ in range(m)]
board = [123] * 123
visited = [False] * 123
board[1] = 0
visited[1] = True


def checkSnake(x):
    for i in snakes:
        if x == i[0]:
            return True


def bfs(x):
    queue = deque()
    queue.append(x)

    while queue:
        cx = queue.popleft()

        for i in range(cx + 1, cx + 7):
            if i >= 101:
                print(board[100])
                exit(0)

            for k in snakes:  # 뱀
                if k[0] == i:
                    if board[k[1]] > board[k[0]]:
                        board[k[1]] = board[k[0]]
                        queue.append(k[1])

            if not visited[i]:
                board[i] = min(board[cx] + 1, board[i])
                visited[i] = True
                if not checkSnake(i):
                    queue.append(i)

            for j in ladder:  # 사다리
                if j[0] == i :
                    board[j[1]] = min(board[j[0]], board[j[1]])
                    queue.append(j[1])



bfs(1)
