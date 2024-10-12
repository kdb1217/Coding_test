


def dfs(n, tmp, c):
    global visited
    global answer
    if n == 6:
        tmp.sort()
        if tmp not in answer:
            answer.append(tmp)

        return

    for i in range(c, len(arr)):
        dfs(n + 1, tmp + [arr[i]], i + 1)




while True:
    arr = list(map(int, input().split()))

    if len(arr) == 1:
        break
    arr.remove(arr[0])
    arr.sort()
    answer = []


    visited = [False] * len(arr)

    dfs(0, [], 0)

    for i in answer:
        print(*i)
    print()