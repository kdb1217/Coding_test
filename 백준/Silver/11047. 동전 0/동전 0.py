n, k = map(int, input().split())
coins = sorted(list(int(input()) for _ in range(n)), reverse=True)
answer = 0

for i in coins:
    answer += k // i
    k %= i

    if k == 0:
        break

print(answer)