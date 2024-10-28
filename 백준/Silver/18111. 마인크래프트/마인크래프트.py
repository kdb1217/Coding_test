n, m, b = tuple(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(n)]
total = 0
time = 213123131
answer = [0,0]

total = b
for i in range(n):
    total += sum(arr[i])

ave = total // (n * m)

for z in range(0, ave + 1):
    ave = z
    tmp = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] > ave:
                tmp += (arr[i][j] - ave) * 2

            if arr[i][j] < ave:
                tmp += (ave - arr[i][j])


    if tmp <= time:
        time = tmp
        answer[0] = time
        answer[1] = max(ave, answer[1])

print(*answer)