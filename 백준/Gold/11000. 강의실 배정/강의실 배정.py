import sys
import heapq

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda x: (x[0], x[1]))

rooms = []
heapq.heappush(rooms, arr[0][1])
for i in range(1, len(arr)):
    if rooms[0] <= arr[i][0]:
        heapq.heappop(rooms)
        heapq.heappush(rooms, arr[i][1])
    else:
        heapq.heappush(rooms, arr[i][1])


print(len(rooms))
