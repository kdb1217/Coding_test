board = [list(map(int, input().split())) for _ in range(19)]

# → ↓ ↘ ↗ 방향 (오른쪽, 아래, 오른쪽 아래, 오른쪽 위)
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

def in_range(x, y):
    return 0 <= x < 19 and 0 <= y < 19

for i in range(19):
    for j in range(19):
        if board[i][j] == 0:
            continue
        color = board[i][j]
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            cnt = 1

            # 이전 돌이 같은 색이면 중복 카운트 → skip
            px = i - dx[d]
            py = j - dy[d]
            if in_range(px, py) and board[px][py] == color:
                continue

            # 현재 방향으로 4개 더 탐색
            while in_range(nx, ny) and board[nx][ny] == color:
                cnt += 1
                if cnt > 5:
                    break
                nx += dx[d]
                ny += dy[d]

            if cnt == 5:
                print(color)
                print(i + 1, j + 1)  # 시작점 출력
                exit()

print(0)