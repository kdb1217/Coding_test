INF = int(1e9)
n, m = map(int, input().split())
dist = [INF] * (n + 1)
edges = []

for _ in range(m):
    start, end, cost = map(int, input().split())
    edges.append((start, end, cost))


def bf(startNode):
    dist[startNode] = 0

    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            destination = edges[j][1]
            costs = edges[j][2]

            if dist[cur] != INF and dist[destination] > dist[cur] + costs:
                dist[destination] = dist[cur] + costs
                if i == n - 1:
                    return True

    return False


result = bf(1)
if result:
    print("-1")
else:
    for i in range(2, n + 1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
