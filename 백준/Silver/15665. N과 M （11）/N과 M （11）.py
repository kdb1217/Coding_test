n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = set()
visited = [False] * len(arr)


def backtracking(depth, num, results, numbers):
    if depth == m:
        strNum = tuple(num)
        if strNum not in results:
            result.add(strNum)
        return

    for i in range(len(arr)):
        backtracking(depth + 1, num + [arr[i]], results, numbers)


backtracking(0, [], result, arr)
answer = sorted(result)
for i in answer:
    print(*i)