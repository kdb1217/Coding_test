from collections import deque

n, m = map(int, input().split())

visited = [False] * 100001
parent = [-1] * 100001
time = [0] * 100001

queue = deque()
queue.append(n)
visited[n] = True

while queue:
    now = queue.popleft()

    if now == m:
        break

    for next_pos in [now - 1, now + 1, now * 2]:
        if 0 <= next_pos <= 100000 and not visited[next_pos]:
            visited[next_pos] = True
            time[next_pos] = time[now] + 1
            parent[next_pos] = now
            queue.append(next_pos)

# 시간 출력
print(time[m])

# 경로 역추적
path = []
curr = m
while curr != -1:
    path.append(curr)
    curr = parent[curr]
path.reverse()
print(*path)