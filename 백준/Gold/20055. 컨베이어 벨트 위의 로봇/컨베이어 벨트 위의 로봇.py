import sys
from collections import deque


def solution():
    n, k = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    belts = []
    for i in range(len(arr)):
        belts.append([arr[i], False])

    firstbelt = deque(belts[:n])
    secondbelt = deque(reversed(belts[n:]))
    time = 0

    # 종료조건 확인
    def isstop():
        zeroCount = 0
        for i in range(len(firstbelt)):
            if firstbelt[i][0] == 0:
                zeroCount += 1
        for i in range(len(secondbelt)):
            if secondbelt[i][0] == 0:
                zeroCount += 1

        if zeroCount >= k:
            print(time)
            exit()

    # 회전하는 함수
    def movetrailier():
        tmp = firstbelt.pop()
        tmp[1] = False
        tmp2 = secondbelt.popleft()
        secondbelt.append(tmp)
        firstbelt.appendleft(tmp2)

        if firstbelt[-1][1]:
            firstbelt[-1][1] = False


    # 로봇을 올리는 함수
    def appendRobot():
        if firstbelt[0][0] > 0:
            firstbelt[0][0] -= 1
            firstbelt[0][1] = True

    # 로봇이 움직이는 함수
    def moveRobot():
        for i in range(len(firstbelt) - 2, -1, -1):
            if firstbelt[i][1]:
                if firstbelt[i + 1][1] == False and firstbelt[i + 1][0] >= 1:
                    firstbelt[i + 1][1] = True
                    firstbelt[i + 1][0] -= 1
                    firstbelt[i][1] = False

        if firstbelt[-1][1]:
            firstbelt[-1][1] = False

    while True:
        time += 1
        movetrailier()
        moveRobot()
        appendRobot()
        isstop()


solution()
