def solution(n):
    ans = 0
    tmp = n
    
    if n == 1:
        return 1
    
    while tmp != 0:
        if tmp % 2 == 1:
            tmp -= 1
            ans += 1
        else:
            tmp /= 2
    
    return ans