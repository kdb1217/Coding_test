import heapq
def solution(n, works):
    heap = []
    answer = 0
    for i in works:
        heapq.heappush(heap, i * -1)
    
    for i in range(n):
        tmp = heapq.heappop(heap)
        if tmp < 0:
            tmp += 1
        heapq.heappush(heap, tmp)
    
    for i in heap:
        answer += i * i
    return answer