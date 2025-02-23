n = int(input())
k = int(input())
visited = [0] * n
cards = []
answers = set()

for _ in range(n):
    cards.append(int(input()))


def backtracking(k, curNums):
    global answers
    global visited

    if len(curNums) == k:
        num = "".join(map(str, curNums))
        if num not in answers:
            answers.add(num)
        return

    for i in range(len(cards)):
        if visited[i] == 0:
            visited[i] = 1
            backtracking(k, curNums + [cards[i]])
            visited[i] = 0


backtracking(k, [])
print(len(answers))