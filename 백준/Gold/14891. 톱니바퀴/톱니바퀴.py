"""
톱니바퀴
단순구현

회전하는 함수 따로 빼기
"""
import copy
from collections import deque


queue = deque()
gears = [None] + [deque(input()) for _ in range(4)]


def rotate(direction, gear):
    if direction == 1:
        tmp = gear.pop()
        gear.appendleft(tmp)
    else:
        tmp = gear.popleft()
        gear.append(tmp)
    return gear


def bfs():
    global queue, gears
    result = copy.deepcopy(queue)
    visited = set()
    while queue:
        gearnumber, direction = queue.popleft()
        visited.add(gearnumber)

        if 1 <= gearnumber - 1 <= 4:
            if gears[gearnumber][-2] != gears[gearnumber - 1][2]:
                if gearnumber - 1 not in visited:
                    queue.append([gearnumber - 1, -direction])
                    result.append([gearnumber - 1, -direction])

        if 1 <= gearnumber + 1 <= 4:
            if gears[gearnumber][2] != gears[gearnumber + 1][-2]:
                if gearnumber + 1 not in visited:
                    queue.append([gearnumber + 1, -direction])
                    result.append([gearnumber + 1, -direction])

    for i in range(len(result)):
        gears[result[i][0]] = rotate(result[i][1], gears[result[i][0]])


def solution():
    answer = 0

    k = int(input())
    rotates = [list(map(int, input().split())) for _ in range(k)]


    for i in range(len(rotates)):
        queue.append([rotates[i][0], rotates[i][1]])
        bfs()

    for j in range(1, len(gears)):
        if gears[j][0] == "1":
            answer += 2 ** (j - 1)
    print(answer)


solution()
