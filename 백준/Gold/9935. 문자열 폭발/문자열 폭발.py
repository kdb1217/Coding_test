from collections import deque
arr = list(input())
bomb = list(input())

answer = []

for i in range(len(arr)):
    answer.append(arr[i])
    if len(answer) < len(bomb):
        continue
    else:
        if arr[i] == bomb[-1]:
            if answer[-(1 + len(bomb) - 1):] == bomb:
                del answer[-(1 + len(bomb) - 1):]


if not answer:
    print("FRULA")
else:
    print("".join(answer))