"""
난 백트레킹의 신이 될꺼야
"""

def solution(k, dungeons):
    max_count = 0
    
    def backtracking(current, visited, current_count):
        nonlocal max_count
        max_count = max(max_count, current_count)
        
        for i in range(len(dungeons)):
            if not visited[i] and current >= dungeons[i][0]:
                visited[i] = True
                backtracking(current - dungeons[i][1], visited, current_count + 1)
                visited[i] = False
            
    
    visited = [False] * len(dungeons)
    backtracking(k, visited, 0)
    return max_count

    