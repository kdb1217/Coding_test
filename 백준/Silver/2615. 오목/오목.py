arr = [list(map(int, input().split())) for _ in range(19)]


def checkWin(color, location):
    di = [-1, 0, 1, 1]
    dj = [1, 1, 0, 1]


    for k in range(len(di)):
        tmpI = location[0]
        tmpJ = location[1]
        cnt = 1
        pastI = tmpI - di[k]
        pastJ = tmpJ - dj[k]

        if 0 <= pastI < 19 and 0 <= pastJ < 19 and arr[pastI][pastJ] == color:
            continue

        for p in range(4):
            tmpI += di[k]
            tmpJ += dj[k]

            if tmpI < 0 or tmpI >= 19 or tmpJ < 0 or tmpJ >= 19:
                tmpI -= di[k]
                tmpJ -= dj[k]
                break

            if arr[tmpI][tmpJ] == color:
                cnt += 1
            else:
                break

        if cnt == 5:
            afterI = tmpI + di[k]
            afterJ = tmpJ + dj[k]

            if 0 <= afterI < 19 and 0 <= afterJ < 19 and arr[afterI][afterJ] == color:
                continue  # 6번째 돌도 같은 색이면 무효 (6목 이상)

            # 정확히 5목일 때만 인정
            print(1 if color == 1 else 2)
            print(location[0] + 1, location[1] + 1)
            exit()


for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] != 0:
            checkWin(arr[i][j], [i, j])

print(0)



