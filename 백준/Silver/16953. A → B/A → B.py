from collections import deque
a, b = map(int, input().split())


def greedy(a, b):
    cnt = 1
    # 맨 끝자리 숫자가 1이면 2가 아니라 1을 추가한 것
    # 그외 에는 전부 2로 나눈 것
    # 2로도 안나누어 떨어지면 못만드는 숫자
    while a < b:
        if b % 10 == 1:
            b //= 10
            cnt += 1
        elif b % 2 == 0:
            b //= 2
            cnt += 1
        else:
            return -1

    if a != b:
        return -1
    return cnt


def bfs(x, target):
    queue = deque([(x, 1)])
    visited = set()

    while queue:
        popResult = queue.popleft()
        num, cnt = popResult[0], popResult[1]

        if num == target:
            return num, cnt

        addOne = int(str(num) + "1")
        multiple = num * 2
        if addOne <= target and addOne not in visited:
            queue.append((addOne, cnt + 1))
            visited.add(addOne)

        if multiple <= target and multiple not in visited:
            queue.append((num * 2, cnt + 1))
            visited.add(multiple)

    return -1, -1


# num, cnt = bfs(a, b)
# print(cnt if num == b else -1)

result = greedy(a, b)
print(result)