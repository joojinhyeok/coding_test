def solution(common):
    answer = 0
    last_element = common[-1]
    
    if (common[1] - common[0]) == (common[2] - common[1]):
        d = common[1] - common[0]
        answer = last_element + d
    else:
        r = common[1] // common[0]
        answer = last_element * r
        
    return answer