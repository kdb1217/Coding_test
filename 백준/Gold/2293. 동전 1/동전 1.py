n, k = tuple(map(int, input().split()))
dptable = [0] * 10001

coin = []
for i in range(n):
    coin.append(int(input()))

coin.sort()


dptable[0] = 1

for i in coin:
    for j in range(i, k + 1):
        dptable[j] += dptable[j - i]

print(dptable[k])