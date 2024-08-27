import re

def getInterSection(dict1, dict2):
    intersection = []
    for key in dict1:
        if key in dict2:
            intersection.append(min(dict1[key], dict2[key]))
    return intersection

def getMaxSection(dict1, dict2):
    union = []
    all_keys = set(dict1.keys()).union(set(dict2.keys()))
    for key in all_keys:
        a = dict1.get(key, 0)
        b = dict2.get(key, 0)
        union.append(max(a, b))
    return union
    
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    dict1 = {}
    dict2 = {}
    
    for i in range(len(str1) - 1):
        tmp = str(str1[i] + str1[i + 1])
        if tmp.isalpha():
            if tmp in dict1:
                dict1[tmp] += 1
            else:
                dict1[tmp] = 1
    
    for j in range(len(str2) - 1):
        tmp = str(str2[j] + str2[j + 1])
        if tmp.isalpha():
            if tmp in dict2:
                dict2[tmp] += 1
            else:
                dict2[tmp] = 1
    
    interSection = getInterSection(dict1,dict2)
    maxSection = getMaxSection(dict1,dict2)

    if sum(maxSection) == 0:
        return(65536)
    answer = int((sum(interSection) / sum(maxSection)) * 65536)
    return answer