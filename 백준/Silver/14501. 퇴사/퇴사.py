
def solution():
    n = int(input())
    days = []
    dptable = [0] * (n + 1)


    for i in range(n):
        days.append(tuple(map(int, input().split())))

    dptable.append(days[0])
    for i in range(n):
        # 상담을 할 수 있는 경우
        if i + days[i][0] <= n:
            dptable[i + days[i][0]] = max(dptable[i + days[i][0]], dptable[i] + days[i][1])
        # 상담을 하지 않는 경우
        dptable[i + 1] = max(dptable[i + 1], dptable[i])

    print(dptable[n])

solution()


