from collections import deque
def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append(0)
    
    if target not in words:
        return 0
    
    while queue:
        tmp = queue.popleft()
        
        for i in range(len(words)):
            if words[i][tmp] == target[tmp] and begin[tmp] != target[tmp]:
                answer += 1
                queue.append(tmp + 1)
                break
    return answer