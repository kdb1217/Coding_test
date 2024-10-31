from collections import deque

m, n, h = tuple(map(int, input().split()))
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
tomatoes = []
answer = 0
flag = False


def bfs(tomatoes):
    queue = deque()
    for i in range(len(tomatoes)):
        queue.append(tomatoes[i])
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    dh = [1, -1]

    while queue:
        th, i, j = queue.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if (0 <= ni < n) and (0 <= nj < m):
                if arr[th][ni][nj] == 0:
                    arr[th][ni][nj] = arr[th][i][j] + 1
                    queue.append([th, ni, nj])

        for z in range(2):
            nh = th + dh[z]
            if 0 <= nh < h:
                if arr[nh][i][j] == 0:
                    arr[nh][i][j] = arr[th][i][j] + 1
                    queue.append([nh, i, j])


for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                tomatoes.append([i, j, k])
            if arr[i][j][k] != -1 and arr[i][j][k] != 1:
                flag = True

if not flag:
    print(0)
    exit()


bfs(tomatoes)

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                print(-1)
                exit()
            answer = max(answer, arr[i][j][k])

print(answer - 1)




