sound = list(input())
answer = ["q"]
duck = ["q", "u", "a", "c", "k"]

def change(current):
    if current == "q":
        return 'u'
    elif current == "u":
        return 'a'
    elif current == "a":
        return 'c'
    elif current == 'c':
        return 'k'
    elif current == "k":
        return 'q'


for i in range(len(sound)):
    if sound[i] not in answer:
        if sound[i] != 'q':
            print(-1)
            exit()
        else:
            answer.append("u")
    else:
        for j in range(len(answer)):
            if sound[i] == answer[j]:
                answer[j] = change(answer[j])
                break

for i in answer:
    if i != 'q':
        print(-1)
        exit()

print(len(answer))
