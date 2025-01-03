def solution(friends, gifts):
    names = {}
    history = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    results = [0] * len(friends)

    for i in range(len(friends)):
        if friends[i] not in names:
            names[friends[i]] = i
    
    for i in gifts:
        giver, getter = i.split()
        history[names[giver]][names[getter]] += 1
        history[names[getter]][names[giver]] -= 1
        
    for i in range(len(history)):
        for j in range(len(history[i])):
            if i == j:
                continue
            if history[i][j] > history[j][i]:
                results[i] += 1
            elif history[i][j] == history[j][i] and sum(history[i]) > sum(history[j]):
                results[i] += 1
    

    return max(results)
