import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if len(scoville) == 1:
            tmp = heapq.heappop(scoville)
            if tmp < K:
                return -1
            else:
                return answer
        tmp1 = heapq.heappop(scoville)
        if tmp1 >= K:
            return answer
        tmp2 = heapq.heappop(scoville)
        newFood = tmp1 + (tmp2 * 2)
        answer += 1
        heapq.heappush(scoville, newFood)
            

    return answer