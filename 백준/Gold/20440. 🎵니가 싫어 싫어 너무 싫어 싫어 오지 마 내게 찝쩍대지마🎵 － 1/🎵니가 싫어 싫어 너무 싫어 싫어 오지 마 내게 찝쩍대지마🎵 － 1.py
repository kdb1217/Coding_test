from collections import defaultdict
n = int(input())
# 입장시간과 퇴장시간이 0 ~ 21억이기 때문에 배열을 통해 관리하면 무조건 메모리 초과가 날듯
# 1. 딕셔너리 딕셔너리를 통해서 관리하면 나중에 취합하는 방법에 대해서 생각해봐야함.
answerDict = defaultdict(int)

for i in range(n):
    start, end = map(int, input().split())
    answerDict[start] += 1
    answerDict[end] -= 1

dictKeys = sorted(answerDict.keys())
start, end = 0, 0
cur = 0
answer = -1
flag = False

for i in dictKeys:
    if answerDict[i] > 0:
        cur += answerDict[i]
        if answer < cur:
            answer = cur
            start = i
            end = i
            # answer를 갱신했을때 확인하는 Flag
            flag = True
    if answerDict[i] < 0:
        cur += answerDict[i]
        if flag:
            end = i
            flag = False

print(answer)
print(start, end)


