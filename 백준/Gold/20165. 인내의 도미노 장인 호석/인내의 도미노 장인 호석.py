from collections import deque
n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
flag = [[False] * m for _ in range(n)]
answer = 0


def solution():
    x, y, attackD = list(input().split())
    attackI = int(x) - 1
    attackJ = int(y) - 1
    defenseI, defenseJ = map(int, input().split())
    defenseI -= 1
    defenseJ -= 1

    if attackD == "E":
        direction = 3
    elif attackD == "W":
        direction = 2
    elif attackD == "S":
        direction = 0
    else:
        direction = 1

    attack(attackI, attackJ, direction)
    defense(defenseI, defenseJ)


def attack(i, j, direction):
    global answer
    tmpNum = board[i][j] - 1
    queue = deque([(i, j)])

    di = [1, -1, 0, 0]
    dj = [0, 0, -1, 1]

    if flag[i][j]:
        return
    else:
        answer += 1
        flag[i][j] = True
        while queue:
            tmp = queue.popleft()
            curI, curJ = tmp[0], tmp[1]
            nI = curI + di[direction]
            nJ = curJ + dj[direction]

            if nI < 0 or nI >= n or nJ < 0 or nJ >= m:
                break

            if flag[nI][nJ] and tmpNum > 1:
                tmpNum -= 1
                queue.append((nI, nJ))

            if not flag[nI][nJ] and tmpNum > 0:
                flag[nI][nJ] = True
                answer += 1
                tmpNum = max(tmpNum - 1, board[nI][nJ] - 1)
                queue.append((nI, nJ))



def defense(i, j):
    flag[i][j] = False
    return



for _ in range(r):
    solution()


print(answer)
for i in range(len(flag)):
    for j in range(len(flag[i])):
        if flag[i][j]:
            print("F", end=" ")
        else:
            print("S", end = " ")
    print()



