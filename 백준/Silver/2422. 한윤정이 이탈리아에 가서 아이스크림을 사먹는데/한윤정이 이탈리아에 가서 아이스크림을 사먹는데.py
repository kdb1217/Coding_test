n, m = map(int, input().split())
iceCreams = [i for i in range(1, (n + 1))]
forbiddenArr = [[False for _ in range(n + 1)] for _ in range(n + 1)]
answer = 0

for _ in range(m):
    ice1, ice2 = map(int, input().split())
    forbiddenArr[ice1][ice2] = True
    forbiddenArr[ice2][ice1] = True

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 1, n + 1):
            if not forbiddenArr[i][j] and not forbiddenArr[i][k] and not forbiddenArr[j][k]:
                answer += 1

print(answer)