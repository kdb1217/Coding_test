def solution(friends, gifts):
    names = {}
    history = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    print(history)
    for i in range(len(friends)):
        if friends[i] not in names:
            names[friends[i]] = i
    
    for i in gifts:
        giver, getter = i.split()
        print(giver, getter)
        history[names[giver]][names[getter]] += 1
            
    print(history)
    answer = 0
    return answer