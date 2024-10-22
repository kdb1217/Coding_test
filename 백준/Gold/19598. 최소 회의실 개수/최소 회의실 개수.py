import heapq

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 회의 시작 시간 순으로 정렬
arr.sort(key=lambda x: (x[0], x[1]))

rooms = []
heapq.heappush(rooms, arr[0][1])

for i in range(1, n):
    # 가장 먼저 끝나는 회의를 꺼냄
    if arr[i][0] >= rooms[0]:
        heapq.heappop(rooms)  # 현재 회의실을 재사용
    heapq.heappush(rooms, arr[i][1])

print(len(rooms))