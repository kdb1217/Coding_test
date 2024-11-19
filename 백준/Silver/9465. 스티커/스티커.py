n = int(input())


def solution():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * (len(arr[0])) for _ in range(2)]

    if n == 1:
        return arr[0][0] if arr[0][0] > arr[1][0] else arr[1][0]
    elif n == 2:
        return arr[0][0] + arr[1][1] if arr[0][0] + arr[1][1] > arr[0][1] + arr[1][0] else arr[0][1] + arr[1][0]


    for i in range(len(arr[0])):
        for j in range(2):
            dp[j][i] = arr[j][i] + max(dp[1 - j][i - 1], dp[1 - j][i - 2])

    return max(dp[0][-1], dp[1][-1])



for _ in range(n):
    answer = solution()
    print(answer)
