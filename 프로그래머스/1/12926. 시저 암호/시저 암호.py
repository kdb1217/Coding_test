def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        s[i] = change(s[i],n)
    answer = "".join(s)

    return answer

def change(z, n):
    if z == " ":
        return " "
    z = ord(z)
    for i in range(n):
        if z == 90:
            z = 65
        elif z == 122:
            z = 97
        else:
            z += 1
    return chr(z)