def solution(people, limit):
    sortedArr = sorted(people, reverse = True)
    answer = 0
    startIdx = 0
    lastIdx = len(people) - 1
    
    while startIdx <= lastIdx:
        if sortedArr[startIdx] + sortedArr[lastIdx] <= limit:
            lastIdx -= 1
            
        startIdx += 1
        answer += 1        
    return answer