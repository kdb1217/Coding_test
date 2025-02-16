n = int(input())


def solution():
    ps = input()
    left = 0
    right = 0

    for i in ps:
        if i == "(":
            left += 1
        else:
            right += 1

        if left < right:
            print("NO")
            return 

    if left == right:
        print("YES")
    else:
        print("NO")


for _ in range(n):
    solution()