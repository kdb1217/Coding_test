a, b = tuple(map(int, input().split()))


def gcd(a, b):
    if a == b:
        return a
    elif a < b:
        a, b = b, a
    while(b > 0):
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))