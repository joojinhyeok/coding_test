def solution(dot):
    i = dot[0]
    j = dot[1]
    
    answer = 0
    
    if i >= 0 and j >= 0:
        answer = 1
    elif i >= 0 and j <= 0:
        answer = 4
    elif i <=0 and j >= 0:
        answer = 2
    else:
        answer = 3
    return answer