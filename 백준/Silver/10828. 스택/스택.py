import sys

num = int(sys.stdin.readline())
answer = []
Stack = []
for i in range(num):
    answer.append(sys.stdin.readline())
    if "push" in answer[i]:
        tmp = answer[i].split(" ")
        tmp[-1] = tmp[-1].replace("\n", "")
        Stack.append(tmp[-1])
    elif "pop" in answer[i]:
        if not Stack:
            print(-1)
        else:
            print(Stack[-1])
            Stack.pop(-1)
    elif "size" in answer[i]:
        print(len(Stack))
    elif "empty" in answer[i]:
        if not Stack:
            print(1)
        else:
            print(0)
    elif "top" in answer[i]:
        if not Stack:
            print(-1)
        else:
            print(Stack[-1])
