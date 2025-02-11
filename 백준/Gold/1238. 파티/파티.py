import heapq

INF = int(1e9)
n, m, x = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]
result = [0] * (n + 1)


for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))


# 구해야 하는 것들
# 1. 각각의 마을에서 도착지까지의 최소 시간
# 2. 도착지에서 각각의 마을로 걸리는 시간
# 3. 제일 많은 시간일 걸리는 학생을 출력

def dijkstra(startNode):
    distances = [INF] * (n + 1)
    distances[startNode] = 0
    queue = []
    heapq.heappush(queue, (0, startNode))

    while queue:
        moveCost, node = heapq.heappop(queue)

        if moveCost > distances[node]:
            continue

        for i in graph[node]:
            newCost = moveCost + i[0]

            if newCost < distances[i[1]]:
                distances[i[1]] = newCost
                heapq.heappush(queue, (newCost, i[1]))

    return distances


for i in range(1, n + 1):
    costResult = dijkstra(i)
    result[i] += costResult[x]

returnResult = dijkstra(x)

for i in range(1, n + 1):
    result[i] += returnResult[i]

print(max(result))