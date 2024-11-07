n, m = tuple(map(int, input().split()))

arr = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
answer = 0


def backtracking(alphas, i, j, cnt):
    global answer
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    answer = max(cnt, answer)
    if answer == 26:
        return


    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if (0 <= ni < n and 0 <= nj < m) and arr[ni][nj] not in alphas:
            alphas.add((arr[ni][nj]))
            backtracking(alphas, ni, nj, cnt + 1)
            alphas.remove((arr[ni][nj]))


backtracking(set(arr[0][0]), 0, 0, 1)
print(answer)
