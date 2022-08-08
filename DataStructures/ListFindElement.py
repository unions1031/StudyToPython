def solution(L, x):
    answer = []
    
    for i in range(0,len(L)):
        if L[i] == x:
            answer.append(i)
            
    if len(answer) < 1:
        answer.append(-1)
    
    return answer

''' 다른 풀이

def solution(L, x):
    if x in L:
        return [i for i, y in enumerate(L) if y == x]
    else:
        return [-1]
    
'''