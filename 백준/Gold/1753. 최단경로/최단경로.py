import heapq

n, m = map(int, input().split())
start = int(input())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    #a 시작 노드 b 도착 노드 c 가중치
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(startNode):
    queue = []
    heapq.heappush(queue, (0, startNode))
    distance[startNode] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = distance[now] + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])