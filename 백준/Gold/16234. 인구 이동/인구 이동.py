"""
인구이동
연합 탐색
 방문 배열을 만들어서 어쩌구 저쩌구 해야하는데 어떻게 해야할지 모르겠당.

연합 이동
"""

from collections import deque

n, l, r = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
cnt = 0



def bfs(i, j):
    global changed
    queue = deque()
    queue.append([i, j])
    visited[i][j] = True
    total = arr[i][j]
    record = [[i, j]]

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    while queue:
        i, j = queue.popleft()

        for z in range(4):
            if 0 <= i + di[z] < n and 0 <= j + dj[z] < n:
                if not visited[i + di[z]][j + dj[z]] and l <= abs(arr[i][j] - arr[i + di[z]][j + dj[z]]) <= r:
                    total += arr[i + di[z]][j + dj[z]]
                    record.append([i + di[z], j + dj[z]])
                    queue.append([i + di[z], j + dj[z]])
                    visited[i + di[z]][j + dj[z]] = True


    total = total // len(record)
    if len(record) >= 2:
        changed = True

    for i, j in record:
        arr[i][j] = total



while True:
    visited = [[False] * n for _ in range(n)]
    changed = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)

    if not changed:
        print(cnt)
        break

    cnt += 1

