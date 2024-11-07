n = int(input())
visited = []

def solution():
    global visited
    arr = sorted(list(input()))
    length = len(arr)
    visited = [False] * length
    backtracking(0, arr, [], length)


def backtracking(num, target, answer, length):

    if num == length:
        print("".join(answer))

    for i in range(length):
        if (i > 0 and target[i] == target[i - 1] and not visited[i - 1]) or visited[i]:
            continue
        visited[i] = True
        backtracking(num + 1, target, answer + [target[i]], length)
        visited[i] = False


for _ in range(n):
    solution()

