from collections import deque
def solution(order):
    answer = []
    side = deque()
    idx = 0
    
    for i in range(1, len(order) + 1):
        if i == order[idx]:
            answer.append(i)
            idx += 1
        else:
            for j in range(len(side) - 1, -1, -1):
                if side[j] == order[idx]:
                    answer.append(side.pop())
                    idx += 1
                else:
                    break
            side.append(i)

            
    for j in range(len(side) - 1, -1, -1):
        if side[j] == order[idx]:
            answer.append(side.pop())
            idx += 1
        else:
            break

    return len(answer)
            
                
                
                    
                    