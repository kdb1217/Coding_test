import copy
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

if n == 1:
    print(max(arr[0]), min(arr[0]))
    exit()

def getMax(gameBoard):
    board = copy.deepcopy(gameBoard[0])
    if n > 1:
        for i in range(1, n):
            tmpboard = copy.deepcopy(board)
            for j in range(3):
                if j == 0:
                    board[j] = max(tmpboard[j] + gameBoard[i][j], tmpboard[1] + gameBoard[i][j])
                elif j == 2:
                    board[j] = max(tmpboard[j] + gameBoard[i][j], tmpboard[j - 1] + gameBoard[i][j])
                else:
                    board[j] = max((tmpboard[j] + gameBoard[i][j]), (tmpboard[j - 1] + gameBoard[i][j]), (tmpboard[j + 1] + gameBoard[i][j]))
        return max(board)
    else:
        return max(gameBoard)



def getMin(gameBoard):
    board = copy.deepcopy(gameBoard[0])
    for i in range(1, n):
        tmpboard = copy.deepcopy(board)
        for j in range(3):
            if j == 0:
                board[j] = min(tmpboard[j] + gameBoard[i][j], tmpboard[j + 1] + gameBoard[i][j])
            elif j == 2:
                board[j] = min(tmpboard[j] + gameBoard[i][j], tmpboard[j - 1] + gameBoard[i][j])
            else:
                board[j] = min((tmpboard[j] + gameBoard[i][j]), (tmpboard[j - 1] + gameBoard[i][j]),
                                (tmpboard[j + 1] + gameBoard[i][j]))
    return min(board)


print(getMax(arr), getMin(arr))