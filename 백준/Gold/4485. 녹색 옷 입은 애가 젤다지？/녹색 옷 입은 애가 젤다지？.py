from collections import deque
cnt = 1

while True:
    n = int(input())

    if n == 0:
        exit(0)

    arr = [list(map(int, input().split())) for _ in range(n)]
    cost = [[1e9] * n for _ in range(n)]
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    queue = deque()
    queue.append([0, 0])
    cost[0][0] = arr[0][0]


    while queue:
        tmp = queue.popleft()
        curI = tmp[0]
        curJ = tmp[1]


        for k in range(4):
            newI = curI + di[k]
            newJ = curJ + dj[k]

            if newI < 0 or newI >= n or newJ < 0 or newJ >= n:
                continue

            newCost = cost[curI][curJ] + arr[newI][newJ]

            if newCost < cost[newI][newJ]:
                cost[newI][newJ] = newCost
                queue.append([newI, newJ])


    print(f"Problem {cnt}: {cost[-1][-1]}")
    cnt += 1






