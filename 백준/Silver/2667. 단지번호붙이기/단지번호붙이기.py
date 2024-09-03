n = int(input())

graph = []
ans = []
num = 2
count = 0

for i in range(n):
    tmp = list(map(int, input()))
    graph.append(tmp)


def dfs(x, y, N, number):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False

    if graph[x][y] == 1:
        graph[x][y] = number
        global count
        count += 1
        dfs(x - 1, y, N, number)
        dfs(x + 1, y, N, number)
        dfs(x, y + 1, N, number)
        dfs(x, y - 1, N, number)
        return True
    return False


for i in range(n):
    for j in range(n):
        if dfs(i, j, n, num):
            ans.append(count)
            num += 1
            count = 0

ans.sort()
print(len(ans))

for i in ans:
    print(i)
