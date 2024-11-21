INF = int(1e9)
n = int(input())
m = int(input())
answers = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            answers[i][j] = 0


for _ in range(m):
    # a는 시작노드, b는 도착노드 c는 비용
    a, b, c = map(int, input().split())
    if answers[a][b] > c:
        answers[a][b] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            answers[i][j] = min(answers[i][j], (answers[i][k] + answers[k][j]))


for i in range(1, len(answers)):
    for j in range(1, len(answers)):
        if answers[i][j] == INF:
            print(0, end=" ")
        else:
            print(answers[i][j], end=" ")
    if i < len(answers) - 1:
        print()