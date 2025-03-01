# 0.3 초
"""
제한
1 ≤ N ≤ 10
1 ≤ M ≤ N^2
1 ≤ K ≤ 1,000
1 ≤ A[r][c] ≤ 100
1 ≤ 입력으로 주어지는 나무의 나이 ≤ 10
입력으로 주어지는 나무의 위치는 모두 서로 다름

풀이 계획
1.우선순위 큐를 써서 각 칸에 여러그루의 나무가 있는 경우 우선순위를 정한다.
2.봄 함수에서 양분만큼 먹지 못한 나무들을 계산하고 바로 여름 함수를 호출한다.
3.
"""
from collections import deque
import heapq

n, m, k = map(int, input().split())
# 배열의 값은 현재의 양분.
board = [list(5 for _ in range(n)) for _ in range(n)]
feedInfo = [list(map(int, input().split())) for _ in range(n)]
treeInfo = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    i, j, age = map(int, input().split())
    treeInfo[i - 1][j - 1].append(age)


def spring():
    canMove = []
    for i in range(n):
        for j in range(n):
            treeInfo[i][j].sort()
            replace = []
            foods = 0
            for k in range(len(treeInfo[i][j])):
                tmp = treeInfo[i][j][k]
                if tmp <= board[i][j]:
                    board[i][j] -= tmp
                    replace.append(tmp + 1)
                    if (tmp + 1) % 5 == 0:
                        canMove.append((i, j))
                else:
                    foods += summer(tmp)

            board[i][j] += foods
            treeInfo[i][j] = replace
    autumn(canMove)


def summer(foods):
    return foods // 2


def autumn(canMoves):


    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]

    for i in range(len(canMoves)):
        x, y = canMoves[i][0], canMoves[i][1]


        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                treeInfo[nx][ny].append(1)


def winter():
    for i in range(n):
        for j in range(n):
            board[i][j] += feedInfo[i][j]


def solution():
    answer = 0

    for _ in range(k):
        spring()
        winter()

    for i in range(n):
        for j in range(n):
            if len(treeInfo[i][j]) > 0:
                answer += len(treeInfo[i][j])

    print(answer)


solution()
