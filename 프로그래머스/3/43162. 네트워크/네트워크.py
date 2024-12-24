from collections import deque
def solution(n, computers):
    cnt = 0
    visited = [False] * n
    def bfs(i):
        queue = deque()
        queue.append(i)
        visited[i] = True
        
        while queue:
            ci = queue.popleft()
            
            for k in range(len(computers[0])):
                if not visited[k]:
                    if computers[ci][k] == 1:
                        queue.append(k)
                        visited[k] = True
    
    for i in range(n):
        if not visited[i]:
            cnt += 1
            bfs(i)
    

    return cnt