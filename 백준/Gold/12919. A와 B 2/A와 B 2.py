from collections import deque

s = list(input())
t = list(input())


def bfs(lst, target):
    queue = deque()
    queue.append(target)

    while queue:
        current = queue.popleft()
        if current == lst:
            return True

        if len(current) > len(s):
            if current[-1] == "A":
                queue.append(current[0:-1])

            if current[0] == "B":
                queue.append(current[:0:-1])

    return False


print(1 if bfs(s, t) else 0)