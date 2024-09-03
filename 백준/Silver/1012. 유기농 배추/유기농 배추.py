import sys

sys.setrecursionlimit(2501)

n = int(input())


def dfs(x, y, col, row, graph):
    if x < 0 or x >= row or y < 0 or y >= col:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x, y - 1, col, row, graph)
        dfs(x, y + 1, col, row, graph)
        dfs(x - 1, y, col, row, graph)
        dfs(x + 1, y, col, row, graph)
        return True
    return False


def solution(col, row, k):
    arr = [[0 for _ in range(col)] for _ in range(row)]
    answer = 0
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    for i in range(row):
        for j in range(col):
            if dfs(i, j, col, row, arr):
                answer += 1
    print(answer)


for _ in range(1, n + 1):
    tmp = list(map(int, input().split()))
    solution(tmp[0], tmp[1], tmp[2])
