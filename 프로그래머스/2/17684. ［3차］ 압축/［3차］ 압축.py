from collections import deque
def solution(msg):

    answer = []
    wordDict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q":17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
    idx = 27
    i = 0
    while i < len(msg):
        tmpWord = msg[i]
        
        while i + 1 < len(msg) and tmpWord + msg[i + 1] in wordDict:
            tmpWord += msg[i + 1]
            i += 1
            
        answer.append(wordDict[tmpWord])
        
        if i + 1 < len(msg):
            wordDict[tmpWord + msg[i + 1]] = idx
            idx += 1
    
        i += 1
            
    return answer
