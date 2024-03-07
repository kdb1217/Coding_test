def solution(x):
    hishard = checkhishard(x)
    if x % hishard == 0:
        return True
    else:
        return False

def checkhishard(x):
    if x < 10:
        return x
    
    return checkhishard(x // 10) + x % 10