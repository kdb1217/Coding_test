def solution(x, n):
    answer = [
        0 for _ in range(n)
    ]
    for i in range(n):
        answer[i] = x
        x += answer[0]
    return answer