n = input()
visited = [False] * len(n)


def solution(s, visited, start, end, ):
    if start >= end:
        return

    minChar = "~"
    minIdx = -1

    for i in range(start, end):
        if not visited[i] and n[i] < minChar:
            minChar = s[i]
            minIdx = i

    visited[minIdx] = True

    for i in range(len(s)):
        if visited[i]:
            print(s[i], end="")
    print()

    solution(s, visited, minIdx + 1, end)
    solution(s, visited, start, minIdx)

    return


solution(n, visited, 0, len(n))

