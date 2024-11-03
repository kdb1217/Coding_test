from collections import deque

n, k = tuple(map(int, input().split()))

arr = [1000000] * (2 * max(n, k) + 1)


def bfs(x):
    queue = deque()
    queue.append(x)
    time = 1
    arr[x] = 0

    while queue:
        tx = queue.popleft()

        if tx * 2 < k + 2:
            if arr[tx] < arr[tx * 2]:
                arr[tx * 2] = arr[tx]
                queue.appendleft(tx * 2)


        if tx - 1 >= 0:
            if arr[tx - 1] > arr[tx] + 1:
                arr[tx - 1] = arr[tx] + 1
                queue.append(tx - 1)

        if tx + 1 < k + 2:
            if arr[tx + 1] > arr[tx] + 1:
                queue.append(tx + 1)
                arr[tx + 1] = arr[tx] + 1

        time += 1
        if tx == k:
            break


bfs(n)
print(arr[k])
