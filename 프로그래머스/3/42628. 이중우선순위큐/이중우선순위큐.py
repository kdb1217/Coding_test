import heapq

def solution(operations):
    maxheap = []
    minheap = []
    heap = []
    for i in range(len(operations)):
        tmp = operations[i].split()
        cmd = tmp[0]
        num = int(tmp[1])
        
        if cmd == "I":
            heapq.heappush(maxheap, num * -1)
            heapq.heappush(minheap, num)
        else:
            if len(maxheap) > 0 and len(minheap) > 0:
                if int(num) == -1:
                    heapq.heappop(minheap)
                    maxheap = list(map(lambda x: x * -1, minheap))
                    heapq.heapify(maxheap)
                else:
                    heapq.heappop(maxheap)
                    minheap = list(map(lambda x: x * -1, maxheap))
                    heapq.heapify(minheap)
                    

    if len(maxheap) == 0:
        return [0,0]
    return [maxheap[0] * -1, minheap[0]] 