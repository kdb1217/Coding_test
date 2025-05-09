from collections import deque

arr = list(input())
targetArr = list(input())
flag = False

"""
풀이 계획
1. 시작부터 끝을 탐색하면 메모리 초과가 뜬다.
2. 그럼 끝부터 처음을 탐색하면?
"""


while len(arr) != len(targetArr):
    if targetArr[-1] == "A":
        targetArr.pop()
    else:
        targetArr.pop()
        targetArr = list(reversed(targetArr))


if arr == targetArr:
    print(1)
else:
    print(0)


