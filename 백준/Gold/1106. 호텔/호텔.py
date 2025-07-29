c, n = map(int, input().split())
info = []
maxNum = int(1e9)
dp = [maxNum] * 1100
dp[0] = 0


for _ in range(n):
    cost, consumer = map(int, input().split())
    info.append((cost, consumer))



for i in range(n):
    for j in range(info[i][1], len(dp)):
        dp[j] = min(dp[j], dp[j - info[i][1]] + info[i][0])

print(min(dp[c:]))

