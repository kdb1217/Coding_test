def solution(n, left, right):
    arr = list(0 for i in range(n))
    answer = []
    if right - left == 0:
        return [0]
    for i in range(left, right + 1):
        answer.append((max(i // n, i % n) + 1))
        
    return answer
