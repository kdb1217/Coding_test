n, m = tuple(map(int, input().split()))
arr = sorted(list(map(int, input().split())))
visited = [False] * n
result = set()


def backtracking(lst):
    if len(lst) == m:
        if tuple(lst) not in result:
            print(*lst)
        result.add(tuple(lst))
        return

    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            backtracking(lst + [arr[i]])
            visited[i] = False


backtracking([])
