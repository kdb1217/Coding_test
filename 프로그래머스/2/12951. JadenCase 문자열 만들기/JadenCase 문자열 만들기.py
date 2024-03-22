def solution(s):
    s = list(s)
    if s[0].isalpha():
        s[0] = s[0].upper()
    for i in range(1,len(s)):
        if s[i - 1].isalpha() or s[i - 1].isdigit():
            s[i] = s[i].lower()
        else:
            s[i] = s[i].upper()
    return "".join(s)


