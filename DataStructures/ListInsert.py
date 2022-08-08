def solution(L, x):
    answer = []
    for i in L:
        if i > x:
            L.insert(L.index(i), x)
            answer = L
            return answer
    
    L.append(x)
    answer = L
    return answer

''' 다른풀이

def solution(L, x):
    answer = L
    index=0
    for i in range(len(L)):
        if L[i]<x:
            index +=1
        else
            break
            
    answer.insert(index,x)
    return answer
    


def solution(L, x):

    for idx, num in enumerate(L):
        if num > x:
            L.insert(idx,x)
            break

        if L[-1] < x:
            L.append(x)
        else:
            pass

    return L
    

def solution(L, x):
    if L[-1] < x :
        L.append(x)
    else:
        for idx, num in enumerate(L):
            if num > x:
                L.insert(idx, x)
                break
                
    return L



def solution(L, x):
    L.append(x)
    return L.sort()


'''