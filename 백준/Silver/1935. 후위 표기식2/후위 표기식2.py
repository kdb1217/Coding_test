n = int(input())
string = list(input())
nums = list()
stack = list()


for i in range(n):
    nums.append(int(input()))


for i in range(len(nums)):
    for j in range(len(string)):
        if string[j].isalpha() and len(string[j]) == 1:
            if ord(string[j]) == 65 + i:
                string[j] = str(nums[i])


for i in range(len(string)):
    if string[i].isdigit():
        stack.append(float(string[i]))
    else:
        b = stack.pop()
        a = stack.pop()
        if string[i] == "*":
            stack.append(a * b)
        elif string[i] == "+":
            stack.append(a + b)
        elif string[i] == "-":
            stack.append(a - b)
        else:
            stack.append(a / b)



print(f'{round(stack[0],2):.2f}')
