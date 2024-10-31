import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
visited2 = [[False for _ in range(n)] for _ in range(n)]

dfs1 = 0
dfs2 = 0


def normalDfs(i, j, g):
    if (i < 0 or i >= n) or (j < 0 or j >= n) or visited[i][j] == True:
        return False

    if arr[i][j] == g and not visited[i][j]:
        visited[i][j] = True
        normalDfs(i + 1, j, g)
        normalDfs(i - 1, j, g)
        normalDfs(i, j + 1, g)
        normalDfs(i, j - 1, g)
        return True

    return False



def specialDfs(i, j, g):
    if (i < 0 or i >= n) or (j < 0 or j >= n) or visited2[i][j]:
        return False

    if g == "B":
        possible = ["B"]
    else:
        possible = ["R", "G"]

    if arr[i][j] in possible and not visited2[i][j]:
        visited2[i][j] = True
        specialDfs(i + 1, j, g)
        specialDfs(i - 1, j, g)
        specialDfs(i, j + 1, g)
        specialDfs(i, j - 1, g)
        return True

    return False


for i in range(len(arr)):
    for j in range(len(arr[i])):
        tmp = arr[i][j]

        if normalDfs(i, j, tmp):
            dfs1 += 1


for i in range(len(arr)):
    for j in range(len(arr[i])):
        tmp = arr[i][j]

        if specialDfs(i, j, tmp):
            dfs2 += 1

print(dfs1, dfs2)
