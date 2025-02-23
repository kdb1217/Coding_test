# A <= 2000 T <= 10000
def manageIndex(idx, a):
    idx %= a
    return idx


def isFinished(sign, t, bCount, dCount):
    if sign == 0:
        if t == bCount:
            return True
        else:
            return False
    else:
        if t == dCount:
            return True
        else:
            return False


def solution():
    a = int(input())
    t = int(input())
    sign = int(input())
    startIdx = 0
    gameRound = 0
    bCount = 0
    dCount = 0
    while True:
        for i in range(4):
            if i % 2 == 0:
                bCount += 1
            else:
                dCount += 1
            if isFinished(sign, t, bCount, dCount):
                return startIdx
            startIdx += 1
            if startIdx >= a:
                startIdx = manageIndex(startIdx, a)


        for i in range(2 * (gameRound + 2)):
            if i < (2 * (gameRound + 2)) // 2:
                bCount += 1
            else:
                dCount += 1
            if isFinished(sign, t, bCount, dCount):
                return startIdx
            startIdx += 1
            if startIdx >= a:
                startIdx = manageIndex(startIdx, a)

        gameRound += 1


print(solution())


