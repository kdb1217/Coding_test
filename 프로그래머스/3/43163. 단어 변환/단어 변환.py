from collections import deque

def isPossible(word, word2):
    wordlst = list(word)
    wordlst2 = list(word2)
    cnt = 0
    
    for i in range(len(wordlst)):
        if wordlst[i] != wordlst2[i]:
            cnt += 1
            
    if cnt == 1:
        return True
    else:
        return False
        

def solution(begin, target, words):
    answer = 0
    visited = set()
    queue = deque()
    queue.append((begin,0))
    
    if target not in words:
        return 0
    
    while queue:
        tmpWord, cnt = queue.popleft()
        
        if tmpWord == target:
            return cnt
        
        for word in words:
            if word not in visited and isPossible(tmpWord, word):
                queue.append((word, cnt + 1))
            
            
    return 0