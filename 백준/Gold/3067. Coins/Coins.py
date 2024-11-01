def solution():
    coinnum = int(input())
    coins = list(map(int, input().split()))
    money = int(input())
    dp = [0] * (money + 2)

    dp[0] = 1

    for k in coins:
        for j in range(k, (money + 1), 1):
            dp[j] += dp[j - k]

    print(dp[money])
    return


n = int(input())

for _ in range(n):
    solution()


