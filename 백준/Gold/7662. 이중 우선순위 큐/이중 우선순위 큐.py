import heapq
import sys

n = int(input())


def solution():
    nums = int(sys.stdin.readline())
    queue = []
    reversedQueue = []
    numsDict = dict()

    for _ in range(nums):
        inputArr = list(sys.stdin.readline().split())
        commend, num = inputArr[0], int(inputArr[1])

        if commend == "D":
            if len(numsDict.keys()) >= 1:
                if num == -1:
                    while True:
                        tmp = heapq.heappop(queue)
                        if tmp in numsDict:
                            numsDict[tmp] -= 1
                            if numsDict[tmp] == 0:
                                del numsDict[tmp]
                            break

                elif num == 1:
                    while True:
                        tmp = -(heapq.heappop(reversedQueue))
                        if tmp in numsDict:
                            numsDict[tmp] -= 1
                            if numsDict[tmp] == 0:
                                del numsDict[tmp]
                            break

        else:
            if num in numsDict:
                numsDict[num] += 1
            else:
                numsDict[num] = 1
            heapq.heappush(queue, num)
            heapq.heappush(reversedQueue, -num)


    result = numsDict.keys()
    if len(result) >= 1:
        while True:
            maxValue = -(heapq.heappop(reversedQueue))
            if maxValue in numsDict:
                break

        while True:
            minValue = heapq.heappop(queue)
            if minValue in numsDict:
                break

        print(maxValue, minValue)
    else:
        print("EMPTY")


for _ in range(n):
    solution()
