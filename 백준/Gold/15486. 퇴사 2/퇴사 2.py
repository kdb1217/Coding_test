n = int(input())
t = [0]
p = [0]




for _ in range(n):
    arr = list(map(int, input().split()))
    t.append(arr[0])
    p.append(arr[1])

dp = [0 for _ in range(t[-1] + n + 1)]

for i in range(n, 0, -1):
    if (i + t[i]) - 1 > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], dp[i + t[i]] + p[i])

print(dp[1])


