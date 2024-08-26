from collections import deque

def solution(progresses, speeds):
    dec = deque(progresses)
    speedDec = deque(speeds)
    answer = []
    while len(dec) > 0:
        for i in range(len(dec)):
            dec[i] += speedDec[i]
        cnt = 0
        while True:
            if len(dec) > 0 and dec[0] >= 100:
                cnt += 1 
                dec.popleft()
                speedDec.popleft()
            else:
                if cnt != 0 :
                    answer.append(cnt)
                break

    return answer