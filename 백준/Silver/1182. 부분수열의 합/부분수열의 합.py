n, s = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
visited = [False] * len(arr)


def backtracking(depth, result, tmp, idx):
    global answer
    global visited

    if result == s:
        answer += 1

    if depth >= len(arr):
        visited = [False] * (n + 1)
        return

    for i in range(idx, len(arr)):
        if not visited[i]:
            visited[i] = True
            backtracking(depth + 1, result + arr[i], tmp + [arr[i]], i)
            visited[i] = False


backtracking(0, 0, [], 0)
if s == 0:
    answer -= 1
print(answer)
