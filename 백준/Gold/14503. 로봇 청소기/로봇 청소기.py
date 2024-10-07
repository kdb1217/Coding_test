"""
풀이 계획
두개의 배열, 청소 완료상태 확인 배열과, 맵 배열을 생성
방향과, dx,dy를 이용해 움직이기
맨 처음 x값과 y값
함수 크게 4개
1. 현재 청소가 안되어 있을 경우에 청소하는 함수
2. 청소한 이후 주변(상,하,좌,우)에 청소할 수 있는 곳이 있는지 찾는 함수 -> Bool

(주변에 청소할 곳이 없는 경우)
    방향을 유지하고 한칸 후진할 수 있는지 확인 yes 1번과정으로 돌아감
    No exit

(주변에 청소하지 않은 공간이 존재하는 경우)
    반시계 방향으로 90도 회전한다. 회전한 후 앞칸이 청소되지 않은 빈칸인 경우 한칸 전진
    1번으로 돌아간다.

clean 함수
자신이 현재 있는 공간이 청소되있는지 확인한 후 청소가 안되어 있으면 청소하는 함수이다.

check함수
현재 칸의 주변 4칸중에 청소되지 않은 빈칸이 있는지 확인하는 함수 bool 값 리턴
인덱스 값 생각

방향 결정 함수
direction에 따라 dx dy를 옮겨주는 함수

changeDircection함수
반시계방향으로 90도 방향 전환을 하는 함수이다

후진 함수
뒤로 한칸 돌아가는 함수 뒤로 돌아갈 수 없다면 exit하는 기능

전진 함수
앞칸이 청소되지 않은 비어있는 경우 한칸 전진한다.
"""


def solution():
    n, m = map(int, input().split())
    y, x, direction = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(n)]

    # 북, 동, 남, 서 (0, 1, 2, 3)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 청소 상태 기록 배열
    cleaned = [[False] * m for _ in range(n)]

    # 현재 위치 청소
    cleaned[y][x] = True
    count = 1  # 청소한 칸의 수

    # 방향을 반시계 방향으로 90도 회전
    def turn_left():
        nonlocal direction
        direction = (direction - 1) % 4

    while True:
        clean_flag = False  # 주변에 청소할 곳이 있는지 여부

        # 1. 현재 위치에서 네 방향을 탐색
        for _ in range(4):
            turn_left()  # 왼쪽으로 회전
            ny = y + dx[direction]
            nx = x + dy[direction]

            # 청소하지 않았고, 벽이 아닌 경우 전진
            if 0 <= ny < n and 0 <= nx < m and not cleaned[ny][nx] and room[ny][nx] == 0:
                y, x = ny, nx
                cleaned[y][x] = True
                count += 1
                clean_flag = True
                break

        # 2. 네 방향 모두 청소할 곳이 없는 경우
        if not clean_flag:
            # 후진 방향 계산
            back_direction = (direction + 2) % 4
            ny = y + dx[back_direction]
            nx = x + dy[back_direction]

            # 후진할 수 있으면 후진
            if 0 <= ny < n and 0 <= nx < m and room[ny][nx] == 0:
                y, x = ny, nx
            # 후진할 수 없으면 작동 멈춤
            else:
                print(count)
                return

solution()