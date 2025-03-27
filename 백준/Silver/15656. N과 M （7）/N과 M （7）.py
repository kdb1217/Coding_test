N, M = map(int, input().split())
arr = list(map(int, input().split()))


arr = sorted(arr)
answer = []
union = []


def backtracking():
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return

    for i in range(N):
        answer.append(arr[i])
        backtracking()
        answer.pop()


backtracking()
