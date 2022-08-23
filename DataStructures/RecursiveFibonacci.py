def solution(x):
    answer = 0

    if x <= 1:
        return x
    else:
        return solution(x-1) + solution(x-2)


''' 다른 풀이

def solution(x):
    return x if x<2 else (solution(x-1) + solution(x-2))
    
def solution(x):
    answer = 0
    fa = 0
    fb = 1
    while x > 0:
        x -= 1
        fa, fb = fb, fa+fb
        answer = fa
    return answer

    
'''