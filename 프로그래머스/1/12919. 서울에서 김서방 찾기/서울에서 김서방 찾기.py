def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            tmp = str(i)
            answer = "김서방은 " + tmp + "에 있다"
    return answer