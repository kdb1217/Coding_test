n = int(input())

arr = []

for _ in range(n):
    tmp = int(input())
    arr.append(tmp)

maxValue = max(arr) + 1


dp = [[0] * 4 for _ in range(maxValue)]

for i in range(0, 4):
    dp[0][i] = 1


for i in range(maxValue):
    for j in range(1, 4):
        dp[i][j] = dp[i][j - 1]
        if i - j >= 0:
            dp[i][j] += dp[i - j][j]

for i in arr:
    print(dp[i][3])

