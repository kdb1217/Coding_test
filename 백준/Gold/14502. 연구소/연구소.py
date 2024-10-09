"""
연구소
dfs, bfs 짬뽕문제 dfs안에 bfs를 넣자
"""
import copy
from collections import deque

n, m = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
blank = []
answer = -1
viruses = []


def bfs(walls):
    global answer
    queue = deque()
    tmpMap = copy.deepcopy(arr)
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    for i in range(len(viruses)):
        queue.append(viruses[i])

    for i in range(len(walls)):
        tmpMap[walls[i][0]][walls[i][1]] = 1

    while queue:
        i, j = queue.popleft()

        for k in range(4):
            if 0 <= i + di[k] < n and 0 <= j + dj[k] < m:
                if tmpMap[i + di[k]][j + dj[k]] == 0:
                    tmpMap[i + di[k]][j + dj[k]] = 2
                    queue.append([(i + di[k]), (j + dj[k])])

    cnt = 0
    for i in range(len(tmpMap)):
        for j in range(len(tmpMap[i])):
            if tmpMap[i][j] == 0:
                cnt += 1

    return cnt




def dfs(n, walls):
    global answer
    if n == 3:
        # bfs돌려서 안전 넓이 구하기
        answer = max(answer, bfs(walls))
        return
    for i in range(len(blank)):
        if not visited[i]:
            visited[i] = True
            dfs(n + 1, walls + [blank[i]])
            visited[i] = False



for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 0:
            blank.append([i, j])
        elif arr[i][j] == 2:
            viruses.append([i, j])

visited = [False] * len(blank)

dfs(0, [])
print(answer)

