n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            arr[i][j] += arr[i - 1][j]
        elif j > i - 1:
            arr[i][j] += arr[i - 1][j - 1]
        else:
            arr[i][j] += max(arr[i - 1][j], arr[i - 1][j - 1])

print(max(arr[-1]))

