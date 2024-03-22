def solution(s):
    s = list(s.split())
    print(s)
    for i in range(len(s)):
        s[i] = checkString(s[i])
    return " ".join(s)

def checkString(s):
    if s[0].isalpha():
        return s[0].upper() + s[1:].lower()
    else:
        return s[0] + s[1:].lower()

