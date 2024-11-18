a = list(input())
b = list(input())

board = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]


for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            board[i][j] = board[i - 1][j - 1] + 1
        else:
            board[i][j] = max(board[i - 1][j], board[i][j - 1])

answer = 0

for i in range(len(board)):
    for j in range(len(board[0])):
        answer = max(answer, board[i][j])


print(answer)