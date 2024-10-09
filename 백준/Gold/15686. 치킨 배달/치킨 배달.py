"""
치킨 배달
"""

n, m = list(map(int, input().split()))
arr = [list(map(int, input().split())) for i in range(n)]
homes = []
stores = []
answer = 1000000


def calculate(lists):
    total = 0
    tmp = 1000000
    for hx,hy in homes:
        for sx,sy in lists:
            tmp = min(tmp, (abs(hx - sx) + abs(hy - sy)))

        total += tmp
        tmp = 1000000
    return total


def dfs(n, lists):
    global answer
    if n == cnt:
        if len(lists) == m:
            answer = min(answer, calculate(lists))
        return

    dfs(n + 1, lists + [stores[n]])
    dfs(n + 1, lists)


for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            homes.append([i, j])
        elif arr[i][j] == 2:
            stores.append([i, j])

cnt = len(stores)

dfs(0, [])
print(answer)
