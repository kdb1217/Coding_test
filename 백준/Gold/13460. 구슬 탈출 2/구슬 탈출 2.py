"""
구슬 탈출
이건 진짜 무조건 백트래킹
경우의 수 4개
좌, 우, 위, 아래
각각의 경우마다 위치를 계산 해주는 함수
게임이 종료됐는지 확인하는 함수
dfs를 통한 백트래킹
3개함수면 끝
"""
import copy

n, m = tuple(map(int, input().split()))
answer = 11
arr = []


def rotate(balls, direction, board):
    arr = copy.deepcopy(board)
    ri, rj = balls[0]
    bi, bj = balls[1]
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]
    hole_r = hole_b = False
    tmp = []
    if direction == 0:
        # 좌
        if rj > bj:
            tmp = [[bi, bj, "B"], [ri, rj, "R"]]
        else:
            tmp = [[ri, rj, "R"], [bi, bj, "B"]]

    elif direction == 1:
        # 우
        if rj < bj:
            tmp = [[bi, bj, "B"], [ri, rj, "R"]]
        else:
            tmp = [[ri, rj, "R"], [bi, bj, "B"]]

    elif direction == 2:
        # 상
        if ri > bi:
            tmp = [[bi, bj, "B"], [ri, rj, "R"]]
        else:
            tmp = [[ri, rj, "R"], [bi, bj, "B"]]

    elif direction == 3:
        # 하
        if bi > ri:
            tmp = [[bi, bj, "B"], [ri, rj, "R"]]
        else:
            tmp = [[ri, rj, "R"], [bi, bj, "B"]]

    for z in range(len(tmp)):
        i, j = tmp[z][0], tmp[z][1]

        while True:
            ni, nj = i + di[direction], j + dj[direction]
            if ni < 0 or ni >= n or nj < 0 or nj >= m or arr[ni][nj] == "#":
                break
            if tmp[z][2] == "B":
                if arr[ni][nj] == "R":
                    break
                elif arr[ni][nj] == "O":
                    hole_b = True
                    arr[i][j] = "."
                    i, j = 0, 0
                    break

            if tmp[z][2] == "R":
                if arr[ni][nj] == "B":
                    break
                elif arr[ni][nj] == "O":
                    hole_r = True
                    arr[i][j] = "."
                    i, j = 0, 0
                    break
            arr[ni][nj] = tmp[z][2]
            arr[i][j] = "."
            i, j = ni, nj
        tmp[z][0], tmp[z][1] = i, j


    tmp.sort(key=lambda x: x[2], reverse=True)
    if hole_b:
        return [[tmp[0][0], tmp[0][1]], [tmp[1][0], tmp[1][1]]], arr, hole_r, True
    else:
        return [[tmp[0][0], tmp[0][1]], [tmp[1][0], tmp[1][1]]], arr, hole_r, False



def dfs(depth, balls, board):
    global answer

    if depth > 10:
        return

    elif answer < depth:
        return

    elif depth <= 10:
        if balls[0] == [0, 0] and balls[1] != [0, 0]:
            answer = min(answer, depth)
            return

    for direction in range(4):
        new_balls, new_board, hole_r, hole_b = rotate(balls, direction, board)

        if hole_b:
            continue
        if hole_r:
            answer = min(answer, depth + 1)
            return
        if new_balls == balls:
            continue
        dfs(depth + 1, new_balls, new_board)





for i in range(n):
    arr.append(list(input()))

for i in range(n):
    for j in range(m):
        if arr[i][j] == "B":
            blueball = [i, j]
        if arr[i][j] == "R":
            redBall = [i, j]
        if arr[i][j] == "O":
            goal = [i,j]

balls = [redBall] + [blueball]
dfs(0, balls, arr)

if answer > 10:
    print(-1)
else:
    print(answer)
