from collections import deque

n, m = tuple(map(int, input().split()))
answer = 5000000
arr = [[] for _ in range(n + 1)]
studentNumber = n + 1

for _ in range(m):
    i, j = tuple(map(int, input().split()))

    arr[i].append(j)
    arr[j].append(i)


def bfs(x):
    global answer, studentNumber
    queue = deque()
    visited = [False for _ in range(n + 1)]
    cnt = 0
    queue.append([x, cnt])
    number = 0
    visited[x] = True

    while queue:
        result = queue.popleft()
        tmp = result[0]
        number += result[1]

        for i in range(len(arr[tmp])):
            if not visited[arr[tmp][i]]:
                queue.append([arr[tmp][i], cnt + 1])
                visited[arr[tmp][i]] = True

        if len(queue) >= 1 and result[1] != queue[0][1]:
            cnt += 1

    if number <= answer:
        if number == answer:
            studentNumber = min(studentNumber, x)
        else:
            studentNumber = x
        answer = number


for i in range(1, len(arr)):
    bfs(i)

print(studentNumber)