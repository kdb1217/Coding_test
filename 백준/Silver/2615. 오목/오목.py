arr = [list(map(int, input().split())) for _ in range(19)]

def checkWin(color, location):
    # ↗ → ↓ ↘ 방향
    di = [-1, 0, 1, 1]
    dj = [1, 1, 0, 1]

    for k in range(4):
        tmpI = location[0]
        tmpJ = location[1]
        cnt = 1

        # 이전 돌이 같은 색이면 중복 → 무시
        pastI = tmpI - di[k]
        pastJ = tmpJ - dj[k]
        if 0 <= pastI < 19 and 0 <= pastJ < 19 and arr[pastI][pastJ] == color:
            continue

        # 4개 더 탐색
        for _ in range(4):
            tmpI += di[k]
            tmpJ += dj[k]
            if 0 <= tmpI < 19 and 0 <= tmpJ < 19 and arr[tmpI][tmpJ] == color:
                cnt += 1
            else:
                break

        # 정확히 5개일 때만 인정
        if cnt == 5:
            # 6번째 돌이 같은 색이면 무효
            afterI = tmpI + di[k]
            afterJ = tmpJ + dj[k]
            if 0 <= afterI < 19 and 0 <= afterJ < 19 and arr[afterI][afterJ] == color:
                continue

            print(1 if color == 1 else 2)
            print(location[0] + 1, location[1] + 1)
            exit()

# 전체 바둑판 탐색
for i in range(19):
    for j in range(19):
        if arr[i][j] != 0:
            checkWin(arr[i][j], (i, j))

print(0)