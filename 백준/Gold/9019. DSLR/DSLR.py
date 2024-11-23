from collections import deque

n = int(input())


def d(number):
    number *= 2
    if number > 9999:
        number %= 10000
    return number


def s(number):
    if number == 0:
        number = 9999
    else:
        number -= 1
    return number


def l(number):
    return (number % 1000) * 10 + number // 1000


def r(number):
    return (number // 10) + (number % 10) * 1000

def bfs(num, target, commends):
    results = set()
    results.add(num)
    queue = deque()
    queue.append((num, commends))

    while queue:
        popResult = queue.popleft()
        num, commends = popResult[0], popResult[1]

        if num == target:
            print(commends)
            return

        tmp = [(d(num), "D"), (s(num), "S"), (l(num), "L"), (r(num), "R")]

        for x, y in tmp:
            if x not in results:
                queue.append((x, commends + y))
                results.add(x)

    return


def solution():
    number, target = map(int, input().split())
    bfs(number, target, "")


for _ in range(n):
    solution()
