def solution(n):
    idx = 1
    while idx <= n:
        if idx ** 2 == n:
            return (idx + 1) ** 2
        idx += 1
    return -1