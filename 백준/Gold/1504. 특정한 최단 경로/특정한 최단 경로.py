import heapq

INF = int(1e9)
n, m = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))
    graph[end].append((cost, start))

a, b = map(int, input().split())


def dijkstra(startNode):
    distance = [INF] * (n + 1)
    distance[startNode] = 0
    queue = []
    heapq.heappush(queue, (0, startNode))

    while queue:
        moveCost, node = heapq.heappop(queue)

        if moveCost > distance[node]:
            continue

        for i in graph[node]:
            newCost = moveCost + i[0]

            if newCost < distance[i[1]]:
                distance[i[1]] = newCost
                heapq.heappush(queue, (newCost, i[1]))

    return distance


startDistance = dijkstra(1)
aDistance = dijkstra(a)
bDistance = dijkstra(b)

startToA = startDistance[a]
startToB = startDistance[b]
startToK = startDistance[-1]
aTob = aDistance[b]
aToK = aDistance[-1]
bToK = bDistance[-1]

answers = [startToA + aTob + bToK, startToB + aTob + aToK, startToA * 2 + startToB + bToK, startToB * 2 + startToA + aToK, (startToA * 2) + (startToB * 2) + startToK, startToA + aTob + startToB + startToK, startToB + aTob + startToA + startToK]
print(min(answers) if min(answers) < INF else -1)
