from queue import PriorityQueue
n = int(input())

arr = list(list(map(int, input().split())) for _ in range(n))

rooms = PriorityQueue()

arr.sort(key=lambda x: (x[0], x[1]))
rooms.put(arr[0][1])

for i in range(1, n):
    if not rooms.empty():
        tmp = rooms.get()
        if arr[i][0] >= tmp:
            rooms.put(arr[i][1])
        else:
            rooms.put(arr[i][1])
            rooms.put(tmp)

print(rooms.qsize())

