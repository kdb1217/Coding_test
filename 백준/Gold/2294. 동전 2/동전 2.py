n, k = tuple(map(int, input().split()))
dptable = [200000] * (1000000)

coin = []
for i in range(n):
    coin.append(int(input()))

coin.sort()

for i in coin:
    dptable[i] = 1

for i in coin:
    for j in range(i, k + 1):
        dptable[j] = min(dptable[j], dptable[j - i] + dptable[i])

print(-1 if dptable[k] == 200000 else dptable[k] )

