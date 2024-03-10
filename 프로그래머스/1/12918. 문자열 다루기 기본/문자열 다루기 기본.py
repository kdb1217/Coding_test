def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    for i in range(len(s)):
        if (ord(s[i]) >= 65 and ord(s[i]) <= 122):
            return False
    
    else:
        return True