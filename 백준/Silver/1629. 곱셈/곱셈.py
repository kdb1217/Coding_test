a, b, c = tuple(map(int, input().split()))

def solution(a, b):
    if b == 1:
        return a % c

    half = solution(a, b // 2)
    half = (half * half) % c

    if b % 2 == 0:
        return half

    if b % 2 == 1:
        return (half * a) % c


answer = solution(a, b)
print(answer)

