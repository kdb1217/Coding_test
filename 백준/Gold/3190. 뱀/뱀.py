from collections import deque
n = int(input())
k = int(input())
apples = list()
for i in range(k):
    apples.append(list(map(int, input().split())))
l = int(input())
direction = 1
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
direcctons = [""] * 10001
times = 0
snakses = deque([[1, 1]])

for i in range(l):
    l, m = tuple(map(str, input().split()))
    l = int(l)
    direcctons[l] = m

while True:
    times += 1
    i, j = snakses[0]
    ci, cj = i + di[direction], j + dj[direction]
    if 0 < ci <= n and 0 < cj <= n and ([ci, cj] not in snakses):
        snakses.appendleft([ci, cj])
        if snakses[0] in apples:
            apples.remove([ci, cj])
        else:
            snakses.pop()

        if direcctons[times] == "D":
            direction = (direction + 1) % 4
        elif direcctons[times] == "L":
            direction = (direction + 3) % 4
    else:
        break

print(times)