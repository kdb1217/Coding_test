n, r, c = tuple(map(int, input().split()))
answer = 0


def solution(N, x, y):
    global answer

    if x == r and y == c:
        print(answer)
        return

    if N == 1:
        answer += 1
        return

    if not (x <= r < x + N and y <= c < y + N):
        answer += N * N
        return

    solution(N // 2, x, y)
    solution(N // 2, x, y + N // 2)
    solution(N // 2, x + N // 2, y)
    solution(N // 2, x + N // 2, y + N // 2)

solution(2 ** n, 0, 0)