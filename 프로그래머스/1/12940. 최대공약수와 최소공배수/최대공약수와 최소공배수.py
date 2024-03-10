def solution(n, m):
    answer = [gcd(n,m), lcm(n,m)]
    return answer

def gcd(n,m):
    if n < m:
        n, m = m, n
    while(m > 0):
        n, m = m, n % m
    return n
    
def lcm(n,m):
    tmp = gcd(n, m)
    return n * m / gcd(n, m)