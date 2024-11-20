import heapq

n = int(input())
bus = int(input())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]

for _ in range(bus):
    # a 시작도시 b 끝도시 c 비용
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(startNode):
    distance = [INF] * (n + 1)
    distance[startNode] = 0
    queue = []
    heapq.heappush(queue, (0, startNode))

    while queue:
        new_distance, node = heapq.heappop(queue)

        if new_distance > distance[node]:
            continue

        for i in graph[node]:
            cost = new_distance + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    return distance



for i in range(1, n + 1):
    result = dijkstra(i)
    for j in range(1, len(result)):
        if result[j] != INF:
            print(result[j], end=" ")
        else:
            print(0, end=" ")
    if i < n:
        print()