n, m = tuple(map(int, input().split()))
arr = sorted(list(map(int, input().split())))
result = set()


def backtracking(lst):
    if len(lst) == m:
        if tuple(lst) not in result:
            print(*lst)
        result.add(tuple(lst))
        return

    for i in range(len(arr)):
        if not lst or arr[i] >= lst[-1]:
            backtracking(lst + [arr[i]])


backtracking([])
