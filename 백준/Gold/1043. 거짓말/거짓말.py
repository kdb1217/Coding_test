from collections import deque

n, m = tuple(map(int, input().split()))
knowPeople = list(map(int, input().split()))
parties = [list(map(int, input().split())) for _ in range(m)]
answer = 0
graph = [[] for _ in range(n + 1)]


if knowPeople[0] == 0:
    answer = m
else:
    peopleSet = set(knowPeople[1:])
    flag = True
    answer = 0



    def bfs(x):
        global peopleSet
        visited = [False] * (n + 1)
        queue = deque()
        queue.append(x)

        while queue:
            tmp = queue.popleft()
            for i in graph[tmp]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    peopleSet.add(i)

    for i in range(len(parties)):
        if len(parties[i]) == 2:
            continue
        for j in range(1, len(parties[i])):
            for k in range(j, len(parties[i])):
                graph[parties[i][j]].append(parties[i][k])
                graph[parties[i][k]].append(parties[i][j])

    for i in list(peopleSet):
        bfs(i)


    for i in range(len(parties)):
        flag = True
        for j in range(1, len(parties[i])):
            if parties[i][j] in peopleSet:
                flag = False
                break
        if flag:
            answer += 1
print(answer)
