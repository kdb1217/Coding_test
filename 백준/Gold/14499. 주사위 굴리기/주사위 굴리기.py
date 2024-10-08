"""
풀이계획
1. dx, dy를 통해 이동방향으로 이동 (지도 밖으로 이동하는 경우에 명령을 무시해야함)
2. 굴린 주사위의 제일 상단 값 출력
 2 - 1: 주사위 계산, 배열
"""
def solution():
    n, m, x, y, k = tuple(map(int, input().split()))
    arr = []
    # 0 제일위, 1 제일 아래 2 왼 3 오 4 앞 5 뒤
    dice = [0] * 6

    for i in range(n):
        arr.append(list(map(int, input().split())))

    commends = list(map(int, input().split()))

    def changeDice(direction):
        if direction == 1:
            dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]
        elif direction == 2:
            dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]
        elif direction == 3:
            dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]
        elif direction == 4:
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]





            # 1, 2, 3, 4 순서로 주기 때문에 첫번째 더미값
    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]

    for i in range(len(commends)):
        # 이 조건에서만 수행
        if 0 <= x + dx[commends[i]] < n and 0 <= y + dy[commends[i]] < m:
            x += dx[commends[i]]
            y += dy[commends[i]]
            changeDice(commends[i])
            if arr[x][y] == 0:
                arr[x][y] = dice[1]
            else:
                dice[1] = arr[x][y]
                arr[x][y] = 0


            # 맨위면에 있는 값 출력
            print(dice[0])
solution()