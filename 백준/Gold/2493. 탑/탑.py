
n = int(input())

towers = list(map(int, input().split()))
answer = [0] * n
stack = []

for i in range(len(towers)):
    while stack:
        if stack[-1][1] < towers[i]:
            stack.pop()
        else:
            answer[i] = stack[-1][0] + 1
            break
    stack.append((i,towers[i]))

print(*answer)





