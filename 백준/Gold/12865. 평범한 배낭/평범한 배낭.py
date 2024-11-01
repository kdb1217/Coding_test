n, k = tuple(map(int, input().split()))

arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

arr.sort(key=lambda x: (x[0], x[1]))
arr = list(reversed(arr))
dp = [0] * (k + 1)

for w, v in arr:
    for i in range(k, w - 1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)

print(dp[k])
