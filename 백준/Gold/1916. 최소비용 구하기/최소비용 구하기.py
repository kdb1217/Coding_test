import heapq

INF = int(1e9)
n = int(input())
m = int(input())


graph = [[] for _ in range(n + 1)]
distances = [INF for _ in range(n + 1)]

for _ in range(m):
    # start 시작도시, end 도착도시 cost 비용
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

start, end = map(int, input().split())


def dijkstra(start, end):
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        cost, distance = heapq.heappop(queue)

        if distances[distance] < cost:
            continue

        for i in graph[distance]:
            newCost = cost + i[1]
            if newCost < distances[i[0]]:
                distances[i[0]] = newCost
                heapq.heappush(queue, (newCost, i[0]))

    print(distances[end])
    return


dijkstra(start, end)
