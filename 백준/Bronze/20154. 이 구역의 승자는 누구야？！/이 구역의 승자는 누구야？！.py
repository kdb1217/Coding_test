letters = {
    "A": 3, "B": 2, "C": 1, "D": 2, "E": 3,
    "F": 3, "G": 3, "H": 3, "I": 1, "J": 1,
    "K": 3, "L": 1, "M": 3, "N": 3, "O": 1,
    "P": 2, "Q": 2, "R": 2, "S": 1, "T": 2,
    "U": 1, "V": 1, "W": 2, "X": 2, "Y": 2,
    "Z": 1
}

n = input()
answer = []

for i in n:
    answer.append(letters[i])

flag = sum(answer) % 10

if flag == 0 or flag % 2 == 0:
    print("You're the winner?")
else:
    print("I'm a winner!")