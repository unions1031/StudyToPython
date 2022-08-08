'''힌트

lower = 0
upper = len(L) - 1
idx = -1
while lower <= upper:
    middle = (lower + upper) // 2
    if L[middle] == target:
        ..
    elif L[middle] < target:
        lower = ..
    else:
        upper = ..
        

입력값 〉	[2, 5, 7, 9, 11], 4
기댓값 〉	-1

'''

def solution(L, x):
    answer = -1    
    lower = 0
    upper = len(L) - 1

    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] == x:
            return middle
        elif L[middle] < x:
            lower = middle + 1
        else:
            upper = middle - 1

    return answer
    
    ''' 다른 풀이
    
    def solution(L, x):
    lower = 0
    upper = len(L) - 1
    idx = -1
    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] == x:
            idx = middle
            break
        elif L[middle] < x:
            lower = middle + 1
        else:
            upper = middle - 1
    return idx
    
    
def solution(L, x):
    low = 0
    high = len(L)-1
    while (low <= high):
        mid = (low+high)//2

        if L[mid] > x:
            high = mid - 1
        elif L[mid] < x:
            low = mid + 1
        else:
            return mid

    return -1
    
    '''