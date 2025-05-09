from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
max_width = 0
pictures_count = 0


def bfs(location):
    global max_width
    global pictures_count
    tmpWidth = 1
    queue = deque()
    queue.append(location)
    visited[location[0]][location[1]] = True
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    while queue:
        cur_location = queue.popleft()
        curi, curj = cur_location[0], cur_location[1]

        for i in range(4):
            newI = curi + di[i]
            newJ = curj + dj[i]

            if newI < 0 or newI >= n or newJ < 0 or newJ >= m:
                continue

            if visited[newI][newJ]:
                continue

            if arr[newI][newJ] == 1:
                tmpWidth += 1
                queue.append([newI, newJ])

            visited[newI][newJ] = True

    if tmpWidth > 0:
        pictures_count += 1
    max_width = max(max_width, tmpWidth)

    return


for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 1:
            bfs([i,j])

print(pictures_count)
print(max_width)




