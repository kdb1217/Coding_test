import sys
limit_number = 1500000
sys.setrecursionlimit(limit_number)


def solution(numbers, target):
    count = 0
    def dfs(depth, total, numbers, target):
        nonlocal count
        if depth == len(numbers):
            if total == target:
                count += 1
            return
        
        dfs(depth + 1, total - numbers[depth], numbers, target)
        dfs(depth + 1, total + numbers[depth], numbers, target)
        
        
    dfs(0, 0, numbers, target)
    return count