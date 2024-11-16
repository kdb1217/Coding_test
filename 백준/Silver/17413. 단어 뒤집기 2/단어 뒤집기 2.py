n = input()
answers = []
# flag가 0일때는 태그가 없는 상태
flag = 0
word = ""
for i in range(len(n)):
    if n[i] == "<":
        flag = 1
        if word != "":
            answers.append("".join(reversed(word)))
        word = "" + n[i]
    elif n[i] == ">":
        flag = 0
        word += n[i]
        answers.append(word)
        word = ""
    elif n[i] == " " and flag == 0:
        answers.append("".join(reversed(word)))
        answers.append(" ")
        word = ""
    else:
        word += n[i]
    if i == len(n) - 1 and (n[i] != "<" and n[i] != ">"):
        answers.append("".join(reversed(word)))

print("".join(answers))
