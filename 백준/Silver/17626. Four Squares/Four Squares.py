n = int(input())

dptable = [50001 for _ in range(n + 1)]
dptable[0] = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        tmp = j * j
        if tmp > i:
            break
        dptable[i] = min(dptable[i], dptable[i - tmp] + 1)
print(dptable[n])