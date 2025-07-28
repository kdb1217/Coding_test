def solution(s, visited, start, end):
    if start >= end:
        return

    minChar = '~'
    minIndex = -1

    for i in range(start, end):
        if not visited[i] and s[i] < minChar:
            minChar = s[i]
            minIndex = i

    visited[minIndex] = True

    for i in range(len(s)):
        if visited[i]:
            print(s[i], end='')
    print()


    solution(s, visited, minIndex + 1, end)
    solution(s, visited, start, minIndex)

    return


s = input()
visited = [False] * len(s)
solution(s, visited, 0, len(s))