n, m = tuple(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(n)]
tests = [list(map(int, input().split())) for _ in range(m)]

for i in range(n):
    for j in range(1,n):
        arr[i][j] += arr[i][j - 1]


for k in range(m):
    answer = 0
    i1, j1, i2, j2 = tests[k][0] - 1, tests[k][1] - 1, tests[k][2] - 1, tests[k][3] - 1
    if j1 > 0:
        for z in range(i1, i2 + 1):
            answer += arr[z][j2] - arr[z][j1 - 1]
    else:
        for z in range(i1, i2 + 1):
            answer += arr[z][j2]

    print(answer)
